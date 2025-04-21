from django.shortcuts import render
from django.http import HttpResponse
from utils.res_code import json_response

# Create your views here.


def hello(request):
    # return render(request, 'hello.html', {'message': 'Hello, World!'})
    return HttpResponse('hello word')
