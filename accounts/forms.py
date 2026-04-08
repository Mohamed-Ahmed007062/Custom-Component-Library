from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with accessibility support."""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'aria-label': 'Email address',
            'aria-required': 'true',
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username',
                'aria-label': 'Username',
                'aria-required': 'true',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'aria-label': 'Password',
            'aria-required': 'true',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password',
            'aria-label': 'Confirm password',
            'aria-required': 'true',
        })


class CustomAuthenticationForm(AuthenticationForm):
    """Custom login form with accessibility support."""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'aria-label': 'Username',
            'aria-required': 'true',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'aria-label': 'Password',
            'aria-required': 'true',
        })
    )


class CustomPasswordResetForm(PasswordResetForm):
    """Custom password reset form with accessibility support."""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
            'aria-label': 'Email address',
            'aria-required': 'true',
        })
    )


class CustomSetPasswordForm(SetPasswordForm):
    """Custom set password form with accessibility support."""
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password',
            'aria-label': 'New password',
            'aria-required': 'true',
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password',
            'aria-label': 'Confirm new password',
            'aria-required': 'true',
        })
    )


class UserUpdateForm(forms.ModelForm):
    """Form for updating user profile."""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'aria-label': 'Email address',
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name',
                'aria-label': 'First name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
                'aria-label': 'Last name',
            }),
        }
