from django.urls import path
from . import views
from .views import TaskListView, TaskListDataView
from utils.r_cache import refresh_memorized_word_ids
urlpatterns = [
    path('categories/', views.get_categories, name='get_categories'),    # get categories API
    path('task_add/', views.AddTaskView.as_view(), name='task_add'),    # add task API
    path('add_task/', views.task_add_page, name='task_add_page'),   # get addtask page
    path('tasks/', TaskListView.as_view(), name='task_list'),    # 任务列表页面
    path('', TaskListView.as_view(), name='task_list'),    # 任务列表页面   根目录跳转到此
    path('tasks_list/', TaskListDataView.as_view(), name='task_list_data'), #    任务列表 API
    path('refresh_memorized_word_ids/', refresh_memorized_word_ids, name='refresh_memorized_word_ids'), # 刷新用户已经认识的单词的id并存入redis
    #手动添加子任务（再来一批）
    path('add_task_batch', views.add_task_batch, name='add_task_another'),
    # add review task
    path('add_review_task/', views.AddReviewTaskView.as_view(), name='add_review_task'),
    path('add_review', views.add_review, name='add_review'),    # 添加复习任务页面的page
]