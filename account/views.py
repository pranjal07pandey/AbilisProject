from django.shortcuts import render
from .models import *
from .forms import DocumentationForm, CategoryForm, DocumentNewForm
from django.shortcuts import get_object_or_404
# from django.contrib import auth
# from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




from rest_framework import viewsets
from .serializers import *


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json

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
            category = Category.objects.all()
            doc_category = DocumentCategory.objects.all()
            context = {'added': True, 'add_category': category, 'add_doc_category': doc_category}

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
    users= user.objects.all()
    count = user.objects.all().count()
    context = {'active_users':users, 'total_users':count}
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def userList(request):
    return render(request, 'userlist.html')


@login_required(login_url='login')
def list_category(request):
    document = Category.objects.all()
    return render(request, 'documents/disable_category/category_list.html', context={'cat_list': document})


@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES or None)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            category = Category.objects.all()
            doc_category = DocumentCategory.objects.all()

            context = {'catadded': True, 'add_category': category, 'add_doc_category': doc_category}

            return render(request, 'documents/document_add.html', context)
    else:
        form = CategoryForm()

    return render(request, 'documents/disable_category/category_add.html', {'from': form})

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
    return render(request, 'documents/disable_category/category_list.html', {'cat_list': delete})


@login_required(login_url='login')
def list_document_category(request):
    document = DocumentCategory.objects.all()
    return render(request, 'documents/document_category/document_category_list.html', context={'doc_list': document})


@login_required(login_url='login')
def add_document_category(request):
    if request.method == "POST":
        form = DocumentNewForm(request.POST, request.FILES or None)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            category = Category.objects.all()
            doc_category = DocumentCategory.objects.all()

            context = {'cat_added': True,'add_category': category, 'add_doc_category': doc_category}

            return render(request, 'documents/document_add.html', context)
    else:
        form = CategoryForm()

    return render(request, 'documents/document_category/document_category_add.html', {'from': form})


@login_required(login_url='login')
def delete_document_category(request, pk):
    delete = get_object_or_404(DocumentCategory, pk=pk)
    delete.delete()
    delete = DocumentCategory.objects.all()
    return render(request, 'documents/document_category/document_category_list.html', {'doc_list': delete})


def logout_user(request):
    logout(request)
    return redirect('login')



#API

# API for User
class UserList(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer


# API for Document Category

class DocumentCategoryList(viewsets.ModelViewSet):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer


# API for Category List

class categoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryinfoSerializer


# API for Documentaion
class DocumentationList(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer


@csrf_exempt
def UserLogin(request):

    username = request.POST['username']
    password = request.POST['password']

    acoountuser = user.objects.filter(username = username , password = password)
    if acoountuser :
        mainuser = user.objects.get(username = username)
        data = serializers.serialize('json', [mainuser, ])
        struct = json.loads(data)
        data = json.dumps(struct[0])
        return HttpResponse(data)
    else:
        return HttpResponse("N")

