# Introduction

KDL_Wagtail provides a new type of Wagtail page for the Archetype site. It is quite generic and can used for many type of 'static' content.

Th package defines a new type of page called 'Section Page'. Within a Section Page, Wagtail Streamfield can be used to create a sequence of Sections. In turn, each section can contain a sequence of Section Items.

Section or a Section Item have a type field which determine which django template is used to render their content.
 
For instance, we have a Home Page (Section Page) 
that starts with an About section (a Section with type = 'about').
The About section contains a testimonial item (A Section Item with type = 'testimonial').

In that example, the about section will use templates/kdl_wagtail/section_about.html.
The testimonial section item will use the templates/kdl_wagtail/section_testimonials_item.html;

# Django template selection algorithm

For a Section of type = STYPE, it tries the following templates in this order:
* section_STYPE.html
* section.html

For a Section Item of type = ITYPE, it tries the following templates in this order:
* section_STYPE_item_ITYPE.html
* section_ITYPE_item.html
* section_item.html

section.html and section_item.html are already defined and also serve as base templates other templates can extend/inherit from.

You'll see in section.html a loop through all items and a delegation to the Section Item templates. This can be overridden and a Section template can, if you prefers, directly render the items without delegation.
