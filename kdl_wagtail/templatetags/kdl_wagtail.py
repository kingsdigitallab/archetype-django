from django import template
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

register = template.Library()


@register.filter()
def kdl_sugar(value):
    return mark_safe(value.replace('%br%', '<br/>'))


@register.simple_tag(takes_context=True)
def smoothscroll(context):
    ret = ''

    import re
    path_info = context.request.path_info
    path = re.sub(r'#.*', '', path_info)
    if path == '/':
        ret = 'smoothscroll'

    return ret


@register.simple_tag(takes_context=True)
def include_block_kdl(context, obj, filter=None):
    '''
    filter: -testimonial,feature => ignore testimonial and feature
          : testimonial => ignore all apart from testimonial
    '''
    block = getattr(obj, 'block', None)
    if block is None:
        return 'Wrong object type passed to include_block_kdl: {}'\
            .format(repr(obj))

    is_section_block = False
    # obj is either:
    if hasattr(obj, 'value'):
        # <StreamChild> for SectionBlock
        value = obj.value
        is_section_block = True
    else:
        # <StructValue> for SectionItemBlock
        value = obj

    obj_type = value['type']

    # Apply type filter is needed
    if filter is not None:
        parts = filter.strip()
        parts = filter.strip('-')
        exclude = (parts != filter)
        parts = parts.split(',')
        if ((obj_type in parts) and exclude) or\
                ((obj_type not in parts) and not exclude):
            return ''

    # Add self and value to the context
    new_context = context.flatten()
    new_context = block.get_context(
        value, parent_context=new_context)

    new_context['self'] = obj

    # Create candidate template paths
    if is_section_block:
        new_context['section_type'] = obj_type
        paths = [
            'section_{}'.format(obj_type),
            'section',
        ]
    else:
        parent = new_context['section_type']
        paths = [
            'section_{}_item_{}'.format(parent, obj_type or parent),
            'section_{}_item'.format(obj_type or parent),
            'section_{}_item'.format(parent),
            'section_item',
        ]

    # print(paths)

    # prefix with path
    paths = ['kdl_wagtail/{}.html'.format(i) for i in paths]

    ret = mark_safe(render_to_string(paths, new_context))

    return ret
