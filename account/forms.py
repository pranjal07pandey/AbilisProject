from django import forms

from .models import Documentation



class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ('title', 'date', 'category','document')





