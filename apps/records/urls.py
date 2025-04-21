from django.urls import path
from . import views
urlpatterns = [
    path('hello', views.hello, name='hello'),    # get categories API
    # 主分类增删改查：
    path('main_sort', views.MainSortAPI.as_view(), name='main_sort'),  # get categories API
    # 主分类页面：
    path('main_sort_page', views.MainSOrtPage.as_view(), name='main_sort_page'),  # 主分类页面
    path('main_sort_page_list', views.MainSOrtPageList.as_view(), name='main_sort_page_delete'),  # 主分类页面

]