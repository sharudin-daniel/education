from .models import CourseComment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = CourseComment
        fields = ('rating', 'description')
