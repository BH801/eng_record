from django.shortcuts import render
from django.http import HttpResponse
from utils.res_code import json_response
from django.views import View
from .models import MainSort

# Create your views here.


def hello(request):
    # return render(request, 'hello.html', {'message': 'Hello, World!'})
    return HttpResponse('hello word')


# 主分类：
# 获取主分类的接口：
class MainSortAPI(View):
    '''获取主分类返回json get'''
    def get(self,requests):
        # 这里可以添加一些逻辑来获取主分类的数据
        # main_sort_data = [
        #     {"id": 1, "name": "主分类1"},
        #     {"id": 2, "name": "主分类2"},
        #     {"id": 3, "name": "主分类3"},
        # ]
        main_sort_data = MainSort.objects.all().values('id', 'name')
        print(main_sort_data)

        return json_response(main_sort_data)
    def post(self,request):
        name = request.POST.get('name')
        note = request.POST.get('note')
        MainSort.objects.create(name=name,notes=note)
        # mainsort.save()
        # new_main_sort.save()
        return json_response(errmsg= "主分类添加成功")

class MainSOrtPage(View):
    def get(self,request):
        return render(request, 'records/addMainSort.html', {'title': '主分类管理'})


