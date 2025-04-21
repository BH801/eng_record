from django.urls import path
from . import views
urlpatterns = [
    path('hello', views.hello, name='hello'),    # get categories API
    # 主分类增删改查：
    path('main_sort', views.MainSortAPI.as_view(), name='main_sort'),  # get categories API
    # 主分类页面：
    path('main_sort_page', views.MainSOrtPage.as_view(), name='main_sort_page'),  # 主分类页面
    path('main_sort_page_list', views.MainSOrtPageList.as_view(), name='main_sort_page_delete'),  # 主分类页面


    # 学习项目管理
    path('study_project', views.StudyProjectManage.as_view(), name='study_project'),  # 学习项目管理
    # 学习项目页面
    path('study_project_page', views.StudyProjectPage.as_view(), name='study_project_page'),  # 学习项目页面
    path('study_project_page_list', views.StudyProjectPageList.as_view(), name='study_project_page_delete'),  # 学习项目页面

]