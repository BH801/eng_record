from django.db import models
from utils.models import BaseModel


class MainSort(BaseModel):
    name = models.CharField(max_length=255, unique=True)  # 主分类名称
    notes = models.TextField(blank=True, null=True)  # 备注


class StudyProject(BaseModel):
    name = models.CharField(max_length=255, unique=True)  # 学习项目名称
    notes = models.TextField(blank=True, null=True)  # 备注
    # main_sort = models.ForeignKey(MainSort, on_delete=models.CASCADE)  # 主分类

class PorjectDetail(BaseModel):
    name = models.CharField(max_length=255,blank=True,null=True )  # 详细分类名称
    notes = models.TextField(blank=True, null=True)  # 备注
    study_project = models.ForeignKey(StudyProject, on_delete=models.CASCADE)  # 学习项目
    score = models.IntegerField(default=0)  # 分数
    c_date = models.DateField(auto_now_add=True)  # 创建日期
    c_time = models.DateTimeField(auto_now=True)  # 更新时间


