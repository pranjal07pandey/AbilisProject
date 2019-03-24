from django.shortcuts import render
from .models import *
from .forms import DocumentationForm, CategoryForm, DocumentNewForm, AnswerForm
from django.shortcuts import get_object_or_404
# from django.contrib import auth
# from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files import File

import os

from rest_framework import viewsets
from .serializers import *


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json


from django.views import generic

from rest_framework import generics
# from django.db.models import Q
from rest_framework.response import Response
from functools import reduce
import operator
from django.db.models import Q


from django.http import JsonResponse

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
            doc = form.cleaned_data['information']
            file_title = form.cleaned_data['title']
            cr = open(file_title + '.txt', 'w')
            cr.write(doc)
            cr.close()
            cr = open(file_title + '.txt', 'r')
            document.info_file.save(file_title + '.txt', File(cr))
            cr.close()
            os.remove(file_title + '.txt')
            selected = request.POST.getlist('category')

            document.save()
            for cat in selected:
                category_added = Category.objects.get(new_category=cat)
                document.category.add(category_added)

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

class QuestionList(viewsets.ModelViewSet):
    queryset = Form_question.objects.all()
    serializer_class = ForumQuestionSerializer


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
        # data2 = {
        #
        #     'error': False,
        # }
        # dump = json.dumps(data2)

        return HttpResponse(data, content_type='json', status=200)
        # return JsonResponse({'error': 'False'}, status=401)
    else:
        return JsonResponse({'error': True}, status=401)


def question_list(request):
    if request.method == 'POST':
        return HttpResponse('Not Authorized')
    else:
        questions = Form_question.objects.all().order_by('-id')
        return render(request, 'forum/question_list.html', context={'questions': questions})


@login_required
def question_answer(request, id):
    question  = Form_question.objects.get(id=id)
    answer = AnswerForm()
    if request.method == 'POST':
        answer = AnswerForm(request.POST)
        ans = answer.save(commit=False)
        ans.question = question
        ans.save()
        return HttpResponse(1)
    else:
        return render(request, 'forum/question_answer.html', context={'question': question, 'answer_forum': answer})


class SearchList(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        category = self.kwargs['category'].lower().split(',')
        # query = reduce(operator.and_, (Q(category__contains=item) for item in user))
        # dirs = Documentation.objects.filter(query)
        # dirs_serializer = DocumentationSerializer(dirs, context={"request": request}, many=True)
        # data = {}
        # data['Category'] = dirs_serializer.data
        print(category)
        document_search = Documentation.objects.filter(category__new_category__in=category)
        print(document_search)
        dirs_serializer = DocumentationSerializer(document_search, context={"request": request}, many=True)
        return Response(dirs_serializer.data)
        # return HttpResponse(1)

@csrf_exempt
def get_user_question(request, name):
    if request.method == 'GET':
        questions = Form_question.objects.filter(user__username=name)
        ques = ForumQuestionSerializer(questions, many=True)
        return JsonResponse(ques.data, status=202, safe=False)

    else:
        return HttpResponse("Not Authorized", status=300)


#APi FOr Username pull Only

class UsernameonlyList(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userpullSerializer



