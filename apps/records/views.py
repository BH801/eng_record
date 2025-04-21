from django.shortcuts import render
from django.http import HttpResponse
from utils.res_code import json_response
from django.views import View
from .models import MainSort
import json

# Create your views here.


def hello(request):
    # return render(request, 'hello.html', {'message': 'Hello, World!'})
    return HttpResponse('hello word')


# 主分类：
# 获取主分类的接口：
class MainSortAPI(View):
    '''获取主分类返回json get'''
    def get(self,requests):
        main_sort_data = MainSort.objects.all().values('id', 'name')
        # print(main_sort_data)

        return json_response(data = list(main_sort_data))
    def post(self,request):
        name = request.POST.get('name')
        note = request.POST.get('note')
        MainSort.objects.create(name=name,notes=note)
        # mainsort.save()
        # new_main_sort.save()
        return json_response(errmsg= "主分类添加成功")
    def delete(self,request):
        post_values = json.loads(request.body.decode('utf-8'))
        id = post_values.get('id')
        try:
            main_sort = MainSort.objects.get(id=int(id))
            main_sort.delete()
            return json_response(errmsg="主分类删除成功")
        except MainSort.DoesNotExist:
            return json_response(errmsg="主分类不存在")


class MainSOrtPage(View):
    def get(self,request):
        return render(request, 'records/addMainSort.html', {'title': '主分类添加'})

class MainSOrtPageList(View):
    def get(self,request):
        return render(request, 'records/main_sort_list.html', {'title': '主分类列表'})


