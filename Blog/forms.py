""" from django import forms
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Comment')) """


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Comment Here', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap styling dynamically to all fields
        for field_name, field in self.fields.items():
            css_classes = 'form-control mb-3'  # Bootstrap styling for consistency
            if isinstance(field.widget, forms.Textarea):  
                css_classes += ' form-textarea'  # Additional styling for textareas
            field.widget.attrs.update({'class': css_classes})