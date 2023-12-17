from django.shortcuts import render
from .forms import TestForm

def index(request):
    my_dict = {
        'insert_something':"views.pyのinsert_something部分です。",
        'name':"miyazaki_dev",
        'form':TestForm(),
        'insert_forms':'初期値',
    }
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    
    return render(request,'webtestapp/index.html',my_dict)