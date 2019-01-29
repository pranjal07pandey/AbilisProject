from django.shortcuts import render
from .models import *
from .forms import DocumentationForm
from django.shortcuts import get_object_or_404
# from django.contrib import auth
# from django.contrib import messages

from django.contrib.auth.decorators import login_required

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
            return render(request, 'documents/document_add.html',context)

    else:
        form = DocumentationForm()

    return render(request, 'documents/document_add.html', {'form': form})

@login_required(login_url='login')
def document_edit(request, pk):
    document = get_object_or_404(Documentation, pk=pk)
    if request.method == "POST":
        form = DocumentationForm(request.POST, request.FILES or None, instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            document = Documentation.objects.all()
            context = {'added': True}

            return render(request, 'documents/document_list.html',context)

    else:
        form = DocumentationForm(instance=document)


    return render(request, 'documents/document_edit.html',{'documents': document})

@login_required(login_url='login')
def document_delete(request, pk):
    document = get_object_or_404(Documentation, pk=pk)
    document.delete()
    document = Documentation.objects.all()
    return render(request, 'documents/document_list.html', {'document': document})

@login_required(login_url='login')
def dashboard(request):
    data = request.POST.get('textbox1')
    context = {'data': data}
    return render(request, 'test.html', context)



