from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def button(text, button_type='primary', size='md', disabled=False, aria_label='', icon='', **kwargs):
    """
    Renders a reusable button component with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% button "Click Me" "primary" "lg" aria_label="Submit form" %}
    
    Args:
        text: Button text
        button_type: Button style (primary, secondary, success, danger, warning, info, light, dark, link)
        size: Button size (sm, md, lg)
        disabled: Whether the button is disabled
        aria_label: Accessible label for screen readers
        icon: Icon class (e.g., 'fas fa-check')
    """
    classes = f'btn btn-{button_type}'
    
    if size == 'sm':
        classes += ' btn-sm'
    elif size == 'lg':
        classes += ' btn-lg'
    
    if disabled:
        classes += ' disabled'
    
    attrs = f'class="{classes}"'
    
    if disabled:
        attrs += ' disabled aria-disabled="true"'
    
    if aria_label:
        attrs += f' aria-label="{aria_label}"'
    
    # Add any additional attributes
    for key, value in kwargs.items():
        if key.startswith('data_'):
            attrs += f' data-{key[5:]}="{value}"'
        else:
            attrs += f' {key}="{value}"'
    
    icon_html = f'<i class="{icon}" aria-hidden="true"></i> ' if icon else ''
    
    return mark_safe(f'<button {attrs}>{icon_html}{text}</button>')


@register.simple_tag
def alert(message, alert_type='info', dismissible=True, aria_label=''):
    """
    Renders a reusable alert component with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% alert "Success message" "success" %}
    
    Args:
        message: Alert message
        alert_type: Alert style (primary, secondary, success, danger, warning, info, light, dark)
        dismissible: Whether the alert can be dismissed
        aria_label: Accessible label for screen readers
    """
    classes = f'alert alert-{alert_type}'
    
    if dismissible:
        classes += ' alert-dismissible fade show'
    
    attrs = f'class="{classes}" role="alert"'
    
    if aria_label:
        attrs += f' aria-label="{aria_label}"'
    
    dismiss_button = ''
    if dismissible:
        dismiss_button = '''
            <button type="button" class="btn-close" data-bs-dismiss="alert" 
                    aria-label="Close alert">
            </button>
        '''
    
    return mark_safe(f'<div {attrs}>{message}{dismiss_button}</div>')


@register.simple_tag
def card(title='', content='', footer='', header_class='', body_class='', footer_class='', **kwargs):
    """
    Renders a reusable card component with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% card "Card Title" "Card content" "Card footer" %}
    
    Args:
        title: Card title
        content: Card content
        footer: Card footer
        header_class: Additional classes for header
        body_class: Additional classes for body
        footer_class: Additional classes for footer
    """
    html = '<div class="card"'
    
    # Add any additional attributes
    for key, value in kwargs.items():
        if key.startswith('data_'):
            html += f' data-{key[5:]}="{value}"'
        else:
            html += f' {key}="{value}"'
    
    html += '>'
    
    if title:
        header_classes = f'card-header {header_class}'.strip()
        html += f'<div class="{header_classes}"><h5 class="card-title mb-0">{title}</h5></div>'
    
    body_classes = f'card-body {body_class}'.strip()
    html += f'<div class="{body_classes}">{content}</div>'
    
    if footer:
        footer_classes = f'card-footer {footer_class}'.strip()
        html += f'<div class="{footer_classes}">{footer}</div>'
    
    html += '</div>'
    
    return mark_safe(html)


@register.simple_tag
def modal(modal_id, title='', content='', footer='', size='md', aria_label=''):
    """
    Renders a reusable modal component with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% modal "myModal" "Modal Title" "Modal content" "Modal footer" %}
    
    Args:
        modal_id: Unique modal ID
        title: Modal title
        content: Modal content
        footer: Modal footer
        size: Modal size (sm, md, lg, xl)
        aria_label: Accessible label for screen readers
    """
    size_class = f'modal-{size}' if size != 'md' else ''
    
    aria_label_attr = f'aria-label="{aria_label}"' if aria_label else f'aria-labelledby="{modal_id}Label"'
    
    html = f'''
    <div class="modal fade {size_class}" id="{modal_id}" tabindex="-1" 
         aria-hidden="true" {aria_label_attr}>
        <div class="modal-dialog">
            <div class="modal-content">
    '''
    
    if title:
        html += f'''
                <div class="modal-header">
                    <h5 class="modal-title" id="{modal_id}Label">{title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" 
                            aria-label="Close modal"></button>
                </div>
        '''
    
    html += f'<div class="modal-body">{content}</div>'
    
    if footer:
        html += f'<div class="modal-footer">{footer}</div>'
    
    html += '''
            </div>
        </div>
    </div>
    '''
    
    return mark_safe(html)


@register.simple_tag
def form_field(field, label='', help_text='', error_message='', **kwargs):
    """
    Renders a form field with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% form_field form.title "Title" "Enter post title" %}
    
    Args:
        field: Django form field
        label: Field label
        help_text: Help text for the field
        error_message: Error message
    """
    field_id = field.id_for_label or f'id_{field.name}'
    
    html = f'<div class="mb-3">'
    
    if label:
        html += f'<label for="{field_id}" class="form-label">{label}</label>'
    
    # Add ARIA attributes to the field
    field_attrs = {
        'class': 'form-control',
        'id': field_id,
        'aria-describedby': f'{field_id}Help' if help_text else '',
    }
    
    if error_message:
        field_attrs['aria-invalid'] = 'true'
        field_attrs['aria-describedby'] = f'{field_id}Error'
    
    # Render the field with attributes
    html += str(field)
    
    if help_text:
        html += f'<div id="{field_id}Help" class="form-text">{help_text}</div>'
    
    if error_message:
        html += f'<div id="{field_id}Error" class="invalid-feedback">{error_message}</div>'
    
    html += '</div>'
    
    return mark_safe(html)


@register.simple_tag
def breadcrumb(items, aria_label='Breadcrumb'):
    """
    Renders a breadcrumb navigation with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% breadcrumb items %}
    
    Args:
        items: List of dicts with 'text', 'url', and 'active' keys
        aria_label: Accessible label for the breadcrumb
    """
    html = f'<nav aria-label="{aria_label}">'
    html += '<ol class="breadcrumb">'
    
    for item in items:
        if item.get('active'):
            html += f'<li class="breadcrumb-item active" aria-current="page">{item["text"]}</li>'
        else:
            html += f'<li class="breadcrumb-item"><a href="{item["url"]}">{item["text"]}</a></li>'
    
    html += '</ol></nav>'
    
    return mark_safe(html)


@register.simple_tag
def pagination(page_obj, aria_label='Page navigation'):
    """
    Renders pagination with accessibility support.
    
    Usage:
        {% load ui_components %}
        {% pagination page_obj %}
    
    Args:
        page_obj: Django paginator page object
        aria_label: Accessible label for the pagination
    """
    if not page_obj.has_other_pages():
        return ''
    
    html = f'<nav aria-label="{aria_label}">'
    html += '<ul class="pagination justify-content-center">'
    
    # Previous button
    if page_obj.has_previous():
        html += f'''
        <li class="page-item">
            <a class="page-link" href="?page={page_obj.previous_page_number()}" 
               aria-label="Previous page">
                <span aria-hidden="true">&laquo;</span>
                <span class="visually-hidden">Previous</span>
            </a>
        </li>
        '''
    else:
        html += '''
        <li class="page-item disabled">
            <span class="page-link" aria-disabled="true">
                <span aria-hidden="true">&laquo;</span>
                <span class="visually-hidden">Previous</span>
            </span>
        </li>
        '''
    
    # Page numbers
    for num in page_obj.paginator.page_range:
        if page_obj.number == num:
            html += f'''
            <li class="page-item active" aria-current="page">
                <span class="page-link">{num}</span>
            </li>
            '''
        elif num > page_obj.number - 3 and num < page_obj.number + 3:
            html += f'''
            <li class="page-item">
                <a class="page-link" href="?page={num}">{num}</a>
            </li>
            '''
    
    # Next button
    if page_obj.has_next():
        html += f'''
        <li class="page-item">
            <a class="page-link" href="?page={page_obj.next_page_number()}" 
               aria-label="Next page">
                <span aria-hidden="true">&raquo;</span>
                <span class="visually-hidden">Next</span>
            </a>
        </li>
        '''
    else:
        html += '''
        <li class="page-item disabled">
            <span class="page-link" aria-disabled="true">
                <span aria-hidden="true">&raquo;</span>
                <span class="visually-hidden">Next</span>
            </span>
        </li>
        '''
    
    html += '</ul></nav>'
    
    return mark_safe(html)


@register.simple_tag
def skip_link(target_id='main-content', text='Skip to main content'):
    """
    Renders a skip link for keyboard navigation.
    
    Usage:
        {% load ui_components %}
        {% skip_link %}
    
    Args:
        target_id: ID of the target element
        text: Skip link text
    """
    html = f'''
    <a class="visually-hidden-focusable" href="#{target_id}">
        {text}
    </a>
    '''
    
    return mark_safe(html)


@register.simple_tag
def accessible_icon(icon_class, aria_label='', decorative=False):
    """
    Renders an accessible icon.
    
    Usage:
        {% load ui_components %}
        {% accessible_icon "fas fa-check" "Success" %}
    
    Args:
        icon_class: Icon CSS class
        aria_label: Accessible label for screen readers
        decorative: Whether the icon is decorative
    """
    if decorative:
        html = f'<i class="{icon_class}" aria-hidden="true"></i>'
    else:
        html = f'<i class="{icon_class}" aria-label="{aria_label}" role="img"></i>'
    
    return mark_safe(html)
