from django import forms
from .models import Employee

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    feedback = forms.CharField(label="Your Feedback", widget=forms.Textarea)

# To add custom class in django forms
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

