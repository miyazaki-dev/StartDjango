from django.shortcuts import render

def index(request):
    my_dict = {
        'insert_something':"views.pyのinsert_something部分です。"
    }
    return render(request,'webtestapp/index.html',my_dict)