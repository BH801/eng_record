from django.db import models


class BaseModel(models.Model):
    """
    基类，公共字段
    """
    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    is_delete = models.BooleanField('逻辑删除', default=False)

    class Meta:
        # 抽象类，用于继承，迁移的时候不创建
        abstract = True