from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel,\
    StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks.struct_block import StructBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.rich_text import RichText, expand_db_html

'''
Page structure:
    SectionPage
        SectionBlock (n x)
            SectionItemBlock (n x)

    LinkPage

section.type and block.type determine the template name

section.type=TYPE1:
    => section_TYPE1.html
    block.type=TYPE2:
        tries in the following order
        => section_TYPE1_item_TYPE2.html (e.g. testimonial_item_right, variant)
        => section_TYPE2_item.html (e.g. item from another section)
        => section_TYPE1_item.html (e.g. testimonial_item, default)
'''

# Wagtail surround all richtext output with a div, we don't want that
RichText.__html__ = lambda self: expand_db_html(self.source)


class GenericBlock(StructBlock):
    type = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    long_title = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False, classname='full')


class SectionItemBlock(GenericBlock):
    image = ImageChooserBlock(required=False)

    class Meta:
        template = ['kdl_wagtail/section__item.html']


class SectionBlock(GenericBlock):
    items = blocks.ListBlock(SectionItemBlock(label='Item', classname='full'))

    class Meta:
        template = ['kdl_wagtail/section.html']

# TODO: Rename this PageSection


class SectionPage(Page):
    body = StreamField([
        ('section', SectionBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'kdl_wagtail/page_section.html'

    class Meta:
        verbose_name = 'Section Page'
        verbose_name_plural = 'Section Pages'


# TODO: Rename this PageLink

class LinkPage(Page):
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    fragment = models.CharField(
        'Fragment Identifier', max_length=255,
        blank=True, null=True,
        help_text='''(Optional) The id of the page fragment you want to link to,
         i.e. the part after # in the URL'''
    )

    content_panels = Page.content_panels + [
        PageChooserPanel('related_page'),
        FieldPanel('fragment'),
    ]

    class Meta:
        verbose_name = 'Link Page'
        verbose_name_plural = 'Link Pages'
