from django.shortcuts import render
from django.http import HttpResponse
from utils.res_code import json_response
from django.views import View
from .models import MainSort,StudyProject
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


# 学习项目：
class StudyProjectManage(View):
    '''add post'''
    def post(self,requests):
        post_values = json.loads(requests.body.decode('utf-8'))
        name = post_values.get('name')
        notes = post_values.get('notes')
        mainsort = StudyProject.objects.create(name=name,notes=notes)
        return json_response(errmsg= "学习项目添加成功")

    ''' list'''
    def get(self,request):
        main_sort_data = StudyProject.objects.all().values('id', 'name','notes','create_time')
        # print(main_sort_data)
        return json_response(data = list(main_sort_data))   # data = [{id:xx,"name":xx,"notes":xx,"createtime":''},...]
    def delete(self,request):
        post_values = json.loads(request.body.decode('utf-8'))
        id = post_values.get('id')
        try:
            mainsort = StudyProject.objects.get(id=int(id))
            mainsort.delete()
            return json_response(errmsg="学习项目删除成功")
        except MainSort.DoesNotExist:
            return json_response(errmsg="学习项目不存在")



class MainSOrtPage(View):
    def get(self,request):
        return render(request, 'records/addMainSort.html', {'title': '主分类添加'})

class MainSOrtPageList(View):
    def get(self,request):
        return render(request, 'records/main_sort_list.html', {'title': '主分类列表'})


# 学习项目添加和列表页面
class StudyProjectPage(View):
    def get(self,request):
        return render(request, 'records/add_study_project.html', {'title': '学习项目添加'})
class StudyProjectPageList(View):
    def get(self,request):
        return render(request, 'records/study_project_list.html', {'title': '学习项目列表'})



# Projectdetail list 和 添加页面
class ProjectDetailPage(View):
    def get(self,request):
        return render(request, 'records/add_project_detail.html', {'title': '项目详细分类添加'})
class ProjectDetailPageList(View):
    def get(self,request):
        return render(request, 'records/project_detail_list.html', {'title': '项目详细分类列表'})

