# Django Blog Components

A collection of reusable, accessible UI components for Django applications.

## Features

- ♿ **Accessibility First**: All components include ARIA attributes and follow WCAG 2.1 guidelines
- 🎨 **Customizable**: Easy to customize with CSS variables and Bootstrap classes
- 📱 **Responsive**: Mobile-first design approach
- 🔧 **Reusable**: Template tags for easy integration
- 📖 **Well Documented**: Comprehensive documentation and examples

## Installation

### As Django App

1. Add `'components'` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'components',
]
```

2. Load the template tags in your templates:

```django
{% load ui_components %}
```

## Components

### Button

Renders a reusable button component with accessibility support.

```django
{% load ui_components %}
{% button "Click Me" "primary" "lg" aria_label="Submit form" %}
```

**Parameters:**
- `text`: Button text
- `button_type`: Button style (primary, secondary, success, danger, warning, info, light, dark, link)
- `size`: Button size (sm, md, lg)
- `disabled`: Whether the button is disabled
- `aria_label`: Accessible label for screen readers
- `icon`: Icon class (e.g., 'fas fa-check')

### Alert

Renders a reusable alert component with accessibility support.

```django
{% load ui_components %}
{% alert "Success message" "success" %}
```

**Parameters:**
- `message`: Alert message
- `alert_type`: Alert style (primary, secondary, success, danger, warning, info, light, dark)
- `dismissible`: Whether the alert can be dismissed
- `aria_label`: Accessible label for screen readers

### Card

Renders a reusable card component with accessibility support.

```django
{% load ui_components %}
{% card "Card Title" "Card content" "Card footer" %}
```

**Parameters:**
- `title`: Card title
- `content`: Card content
- `footer`: Card footer
- `header_class`: Additional classes for header
- `body_class`: Additional classes for body
- `footer_class`: Additional classes for footer

### Modal

Renders a reusable modal component with accessibility support.

```django
{% load ui_components %}
{% modal "myModal" "Modal Title" "Modal content" "Modal footer" %}
```

**Parameters:**
- `modal_id`: Unique modal ID
- `title`: Modal title
- `content`: Modal content
- `footer`: Modal footer
- `size`: Modal size (sm, md, lg, xl)
- `aria_label`: Accessible label for screen readers

### Form Field

Renders a form field with accessibility support.

```django
{% load ui_components %}
{% form_field form.title "Title" "Enter post title" %}
```

**Parameters:**
- `field`: Django form field
- `label`: Field label
- `help_text`: Help text for the field
- `error_message`: Error message

### Breadcrumb

Renders a breadcrumb navigation with accessibility support.

```django
{% load ui_components %}
{% breadcrumb items %}
```

**Parameters:**
- `items`: List of dicts with 'text', 'url', and 'active' keys
- `aria_label`: Accessible label for the breadcrumb

### Pagination

Renders pagination with accessibility support.

```django
{% load ui_components %}
{% pagination page_obj %}
```

**Parameters:**
- `page_obj`: Django paginator page object
- `aria_label`: Accessible label for the pagination

### Skip Link

Renders a skip link for keyboard navigation.

```django
{% load ui_components %}
{% skip_link %}
```

**Parameters:**
- `target_id`: ID of the target element
- `text`: Skip link text

### Accessible Icon

Renders an accessible icon.

```django
{% load ui_components %}
{% accessible_icon "fas fa-check" "Success" %}
```

**Parameters:**
- `icon_class`: Icon CSS class
- `aria_label`: Accessible label for screen readers
- `decorative`: Whether the icon is decorative

## Accessibility Features

All components include the following accessibility features:

- **ARIA Labels**: Descriptive labels for screen readers
- **ARIA Roles**: Proper semantic roles for interactive elements
- **ARIA States**: Dynamic state announcements (expanded, disabled, etc.)
- **Keyboard Navigation**: Full keyboard support
- **Focus Management**: Visible focus indicators
- **Screen Reader Support**: Hidden text for context
- **High Contrast Support**: Works with high contrast modes
- **Reduced Motion Support**: Respects user preferences

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License
