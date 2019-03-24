from django import forms
# from multiselectfield import MultiSelectFormField

from .models import Documentation, Category, DocumentCategory, Form_answer



class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ('title', 'date', 'doc_category', 'document', 'description', 'information', 'info_file')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('new_category',)


class DocumentNewForm(forms.ModelForm):
    class Meta:
        model = DocumentCategory
        fields = ('doc_category',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Form_answer
        fields = ('answer', )


