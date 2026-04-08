# Django Blog Application

A fully functional web application built with Django that includes user authentication (login, registration, and password reset) and a blog system with reusable, accessible UI components.

## Features

### Authentication System
- ✅ User registration with email validation
- ✅ User login with session management
- ✅ Password reset via email
- ✅ User profile management
- ✅ Secure password validation

### Blog System
- ✅ Create, edit, and delete blog posts
- ✅ Category management
- ✅ Comment system
- ✅ Search functionality
- ✅ Pagination
- ✅ Featured images with alt text

### Accessibility Features
- ♿ WCAG 2.1 AA compliant
- ♿ ARIA labels and roles throughout
- ♿ Keyboard navigation support
- ♿ Screen reader friendly
- ♿ Skip links for keyboard users
- ♿ High contrast mode support
- ♿ Reduced motion support
- ♿ Focus indicators

### Reusable Components
- 🎨 Button component with multiple styles
- 🎨 Alert component with dismissible option
- 🎨 Card component with header, body, footer
- 🎨 Modal component with accessibility
- 🎨 Form field component with labels and help text
- 🎨 Breadcrumb navigation
- 🎨 Pagination component
- 🎨 Skip link component
- 🎨 Accessible icon component

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- Pillow (for image handling)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd django-blog
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django pillow
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
blog_project/
├── blog/                    # Blog application
│   ├── models.py           # Blog models (Post, Category, Comment)
│   ├── views.py            # Blog views
│   ├── forms.py            # Blog forms
│   ├── urls.py             # Blog URLs
│   └── admin.py            # Admin configuration
├── accounts/                # Authentication application
│   ├── views.py            # Authentication views
│   ├── forms.py            # Authentication forms
│   └── urls.py             # Authentication URLs
├── components/              # Reusable UI components
│   ├── templatetags/       # Template tags
│   │   └── ui_components.py # UI component template tags
│   ├── README.md           # Component documentation
│   ├── storybook.html      # Storybook documentation
│   └── package.json        # NPM package configuration
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── blog/               # Blog templates
│   └── accounts/           # Authentication templates
├── static/                  # Static files
├── media/                   # Media files
├── blog_project/            # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URLs
│   └── wsgi.py             # WSGI configuration
└── manage.py                # Django management script
```

## Usage

### Using Reusable Components

Load the template tags in your templates:
```django
{% load ui_components %}
```

#### Button
```django
{% button "Click Me" "primary" "lg" aria_label="Submit form" %}
```

#### Alert
```django
{% alert "Success message" "success" %}
```

#### Card
```django
{% card "Card Title" "Card content" "Card footer" %}
```

#### Modal
```django
{% modal "myModal" "Modal Title" "Modal content" "Modal footer" %}
```

#### Form Field
```django
{% form_field form.title "Title" "Enter post title" %}
```

#### Breadcrumb
```django
{% breadcrumb items %}
```

#### Pagination
```django
{% pagination page_obj %}
```

#### Skip Link
```django
{% skip_link %}
```

#### Accessible Icon
```django
{% accessible_icon "fas fa-check" "Success" %}
```

## Accessibility

This application follows WCAG 2.1 AA guidelines and includes:

- **ARIA Labels**: All interactive elements have descriptive labels
- **ARIA Roles**: Proper semantic roles for components
- **ARIA States**: Dynamic state announcements
- **Keyboard Navigation**: Full keyboard support
- **Focus Management**: Visible focus indicators
- **Screen Reader Support**: Hidden text for context
- **High Contrast Support**: Works with high contrast modes
- **Reduced Motion Support**: Respects user preferences

## Storybook Documentation

View the component documentation by opening `components/storybook.html` in your browser. The Storybook includes:

- Component previews
- Code examples
- Parameter documentation
- Accessibility features

## NPM Package

The components can be packaged as an NPM package for reuse in other projects:

```bash
cd components
npm pack
```

## Testing

Run the Django test suite:
```bash
python manage.py test
```

## Deployment

### Production Settings

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up email backend for password reset

### Static Files

```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework
- Bootstrap for styling
- Font Awesome for icons
- WCAG guidelines for accessibility

## Support

For support, please open an issue in the repository or contact the development team.

## Roadmap

- [ ] Add more component variants
- [ ] Implement dark mode
- [ ] Add unit tests for components
- [ ] Create Storybook integration
- [ ] Add TypeScript support
- [ ] Implement component theming
- [ ] Add animation options
- [ ] Create component playground
