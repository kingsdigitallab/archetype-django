# Introduction

KDL_Wagtail is a package made for creating Archetype page content with Wagtail.

It defines a new type of page called 'Section Page'.
Wagtail Streamfield can be used to create a sequence of Sections within a Section Page.
Each section can contain a sequence of Section Items.

Section or a Section Item have a type field which determine which django template
is used to render their content.
 
For instance, we have a Home Page (Section Page) 
that starts with an About section (a Section with type = 'about').
The About section contains a testimonial item (A Section Item with type = 'testimonial').

In that example, the about section will use templates/kdl_wagtail/section_about.html.
The testimonial section item will use the templates/kdl_wagtail/section_testimonials_item.html;

# Exact algorithm for django template selection

For a Section of type = STYPE, it tries the following templates in this order:
* section_STYPE.html
* section.html

For a Section Item of type = ITYPE, it tries the following templates in this order:
* section_STYPE_item_ITYPE.html
* section_ITYPE_item.html
* section_item.html

section.html and section_item.html are already defined and serve as base templates
the more specific ones can inherit from.

You'll in section.html that there is a loop through all items and a delegation to
the Section Item templates. This can be overridden and a Section template can,
if you prefers, directly render the items without delegation.
