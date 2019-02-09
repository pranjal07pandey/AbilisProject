from django.shortcuts import render
from .models import *
from .forms import DocumentationForm, CategoryForm, DocumentNewForm
from django.shortcuts import get_object_or_404
# from django.contrib import auth
# from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.


@login_required(login_url='login')
def document_list(request):
    document = Documentation.objects.all()
    return render(request, 'documents/document_list.html', context={'document': document})


@login_required(login_url='login')
def document_new(request):
    if request.method == "POST":
        form = DocumentationForm(request.POST, request.FILES or None)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            context = {'added': True}
            return render(request, 'documents/document_add.html', context)
        else:
            print(form.errors)

    else:
        form = DocumentationForm()
        category = Category.objects.all()
        doc_category = DocumentCategory.objects.all()

        return render(request, 'documents/document_add.html', {'form': form, 'add_category': category, 'add_doc_category': doc_category})


@login_required(login_url='login')
def document_edit(request, pk):
    document = get_object_or_404(Documentation, pk=pk)

    if request.method == "POST":

        form = DocumentationForm(request.POST, request.FILES or None, instance=document)
        print("validated form")

        if form.is_valid():

            document = form.save(commit=False)
            document.save()
            document = Documentation.objects.all()
            context = {'added': True,'document':document}
            return render(request, 'documents/document_list.html', context)

    else:
        form = DocumentationForm(instance=document)
        category1 = Category.objects.all()
        doc_category1 = DocumentCategory.objects.all()

        return render(request, 'documents/document_edit.html', {'document': document, 'add_category': category1, 'add_doc_category': doc_category1})


@login_required(login_url='login')
def document_delete(request, pk):
    document = get_object_or_404(Documentation, pk=pk)
    document.delete()
    document = Documentation.objects.all()
    return render(request, 'documents/document_list.html', {'document': document})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'test.html')


@login_required(login_url='login')
def userList(request):
    return render(request, 'userlist.html')


@login_required(login_url='login')
def list_category(request):
    document = Category.objects.all()
    return render(request, 'documents/category_list.html', context={'cat_list': document})


@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES or None)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            context = {'catadded': True}

            return render(request, 'documents/document_add.html', context)
    else:
        form = CategoryForm()

    return render(request, 'documents/category_add.html', {'from': form})

#
# def edit_category(request, pk):
#     edit = get_object_or_404(AddCategory, pk=pk)
#     if request.method == "POST":
#         form = AddCategoryForm(request.POST, request.FILES or None, instance=edit)
#         if form.is_valid():
#             edit = form.save(commit=False)
#             edit.save()
#             edit = AddCategory.objects.all()
#             context = {'added': True,'edit':edit}
#             return render(request, 'documents/document_list.html',context)
#
#     else:
#         form = AddCategoryForm(instance=edit)
#
#
#     return render(request, 'documents/document_edit.html',{'edit': edit})


@login_required(login_url='login')
def delete_category(request, pk):
    delete = get_object_or_404(Category, pk=pk)
    delete.delete()
    delete = Category.objects.all()
    return render(request, 'documents/document_add.html', {'delete': delete})


@login_required(login_url='login')
def list_document_category(request):
    document = DocumentCategory.objects.all()
    return render(request, 'documents/document_category_list.html', context={'doc_list': document})


@login_required(login_url='login')
def add_document_category(request):
    if request.method == "POST":
        form = DocumentNewForm(request.POST, request.FILES or None)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            context = {'cat_added': True}

            return render(request, 'documents/document_add.html', context)
    else:
        form = CategoryForm()

    return render(request, 'documents/document_category_add.html', {'from': form})


@login_required(login_url='login')
def delete_document_category(request, pk):
    delete = get_object_or_404(DocumentCategory, pk=pk)
    delete.delete()
    delete = DocumentCategory.objects.all()
    return render(request, 'documents/document_add.html', {'delete': delete})


def logout_user(request):
    logout(request)
    return redirect('login')
