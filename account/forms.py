from django import forms

from .models import Documentation, Category, DocumentCategory



class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ('title', 'date', 'category', 'doc_category', 'document', 'description', 'information')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('new_category',)

class DocumentNewForm(forms.ModelForm):
    class Meta:
        model = DocumentCategory
        fields = ('doc_category',)



