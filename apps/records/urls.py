from django.urls import path
from . import views,view2
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


    # 学习项目明细管理页面：
    path('project_detail_list', views.ProjectDetailPageList.as_view(), name='project_detail'),  # 学习项目明细管理
    path('project_detail_page', views.ProjectDetailPage.as_view(), name='project_detail_page'),  # 学习项目明细页面
    path('api/project_detail/add', view2.add_project_detail, name='add_project_detail'),
    path('api/project_detail/update', view2.update_project_detail, name='update_project_detail'),
    path('api/project_detail/list', view2.get_project_detail_list, name='get_project_detail_list'),

]