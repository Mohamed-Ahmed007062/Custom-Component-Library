from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts with accessibility support."""
    
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'excerpt', 'featured_image', 'status', 'aria_label', 'alt_text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title',
                'aria-label': 'Post title',
                'aria-required': 'true',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'aria-label': 'Post category',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...',
                'aria-label': 'Post content',
                'aria-required': 'true',
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of your post',
                'aria-label': 'Post excerpt',
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'form-control',
                'aria-label': 'Featured image',
                'accept': 'image/*',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'aria-label': 'Post status',
            }),
            'aria_label': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Accessible label for screen readers',
                'aria-label': 'ARIA label',
            }),
            'alt_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Alternative text for image',
                'aria-label': 'Image alt text',
            }),
        }


class CommentForm(forms.ModelForm):
    """Form for adding comments with accessibility support."""
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...',
                'aria-label': 'Comment content',
                'aria-required': 'true',
            }),
        }
