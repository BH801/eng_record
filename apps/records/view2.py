from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils import timezone
import json
import logging
from datetime import datetime
from .models import PorjectDetail, StudyProject

logger = logging.getLogger(__name__)


@ensure_csrf_cookie
@require_http_methods(["POST"])
def add_project_detail(request):
    """
    添加学习项目明细
    """
    try:
        # 获取并解析请求数据
        data = json.loads(request.body)

        # 必填字段验证
        required_fields = ['study_project', 'score', 'c_datetime']
        for field in required_fields:
            if field not in data:
                return JsonResponse({
                    "errno": "1",
                    "errmsg": f"缺少必填字段: {field}"
                })

        # 验证学习项目是否存在
        try:
            study_project = StudyProject.objects.get(id=data['study_project'])
        except StudyProject.DoesNotExist:
            return JsonResponse({
                "errno": "1",
                "errmsg": "学习项目不存在"
            })

        # 验证名称是否已存在
        if PorjectDetail.objects.filter(name=data['name']).exists():
            return JsonResponse({
                "errno": "1",
                "errmsg": "该名称已存在"
            })

        # 验证分数范围
        try:
            score = int(data['score'])
            if score < 0:
                return JsonResponse({
                    "errno": "1",
                    "errmsg": "分数不能为负数"
                })
        except ValueError:
            return JsonResponse({
                "errno": "1",
                "errmsg": "分数必须为整数"
            })

        # 验证日期格式
        try:
            # c_date = datetime.strptime(data['c_date'], '%Y-%m-%d').date()
            # 这里改成校验datetime格式
            c_datetime= datetime.strptime(data['c_datetime'], '%Y-%m-%d %H:%M')
            c_date  = c_datetime.date()
            c_time = c_datetime
        except ValueError:
            return JsonResponse({
                "errno": "1",
                "errmsg": "日期格式不正确，应为YYYY-MM-DD"
            })

        # 创建新记录
        with transaction.atomic():
            project_detail = PorjectDetail.objects.create(
                name=data['name'],
                study_project=study_project,
                score=score,
                notes=data.get('notes', ''),
                c_date=c_date,
                c_time=c_time,
            )

        return JsonResponse({
            "errno": "0",
            "errmsg": "",
            "data": {
                "id": project_detail.id,
                "name": project_detail.name,
                "create_time": project_detail.c_time.strftime("%Y-%m-%d %H:%M:%S")
            }
        })

    except Exception as e:
        logger.error(f"添加学习项目明细失败: {str(e)}", exc_info=True)
        return JsonResponse({
            "errno": "1",
            "errmsg": "系统错误，请联系管理员"
        })


@ensure_csrf_cookie
@require_http_methods(["POST"])
def update_project_detail(request):
    """
    修改学习项目明细
    """
    try:
        # 获取并解析请求数据
        data = json.loads(request.body)

        # 验证ID是否存在
        if 'id' not in data:
            return JsonResponse({
                "errno": "1",
                "errmsg": "缺少ID参数"
            })

        # 查找要修改的记录
        try:
            project_detail = PorjectDetail.objects.get(id=data['id'])
        except PorjectDetail.DoesNotExist:
            return JsonResponse({
                "errno": "1",
                "errmsg": "记录不存在"
            })

        # 如果修改了学习项目，验证新的学习项目是否存在
        if 'study_project' in data:
            try:
                study_project = StudyProject.objects.get(id=data['study_project'])
                project_detail.study_project = study_project
            except StudyProject.DoesNotExist:
                return JsonResponse({
                    "errno": "1",
                    "errmsg": "学习项目不存在"
                })

        # 如果修改了名称，验证是否与其他记录重复
        if 'name' in data and data['name'] != project_detail.name:
            if PorjectDetail.objects.filter(name=data['name']).exists():
                return JsonResponse({
                    "errno": "1",
                    "errmsg": "该名称已存在"
                })
            project_detail.name = data['name']

        # 更新分数
        if 'score' in data:
            try:
                score = int(data['score'])
                if score < 0:
                    return JsonResponse({
                        "errno": "1",
                        "errmsg": "分数不能为负数"
                    })
                project_detail.score = score
            except ValueError:
                return JsonResponse({
                    "errno": "1",
                    "errmsg": "分数必须为整数"
                })

        # 更新日期
        if 'c_date' in data:
            try:
                c_date = datetime.strptime(data['c_date'], '%Y-%m-%d').date()
                project_detail.c_date = c_date
            except ValueError:
                return JsonResponse({
                    "errno": "1",
                    "errmsg": "日期格式不正确，应为YYYY-MM-DD"
                })

        # 更新备注
        if 'notes' in data:
            project_detail.notes = data['notes']

        # 保存修改
        with transaction.atomic():
            project_detail.save()

        return JsonResponse({
            "errno": "0",
            "errmsg": "",
            "data": {
                "id": project_detail.id,
                "name": project_detail.name,
                "update_time": project_detail.c_time.strftime("%Y-%m-%d %H:%M:%S")
            }
        })

    except Exception as e:
        logger.error(f"修改学习项目明细失败: {str(e)}", exc_info=True)
        return JsonResponse({
            "errno": "1",
            "errmsg": "系统错误，请联系管理员"
        })


@ensure_csrf_cookie
@require_http_methods(["GET"])
def get_project_detail_list(request):
    """
    获取学习项目明细列表
    支持按名称搜索和分页
    """
    try:
        # 获取查询参数
        search_name = request.GET.get('search_name', '')
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))

        # 构建查询
        query = PorjectDetail.objects.select_related('study_project').all()

        # 按名称搜索
        if search_name:
            query = query.filter(name__icontains=search_name)

        # 计算总记录数
        total_count = query.count()

        # 分页
        start = (page - 1) * page_size
        end = start + page_size
        details = query.order_by('-c_time')[start:end]

        # 构建返回数据
        data = []
        for detail in details:
            data.append({
                "id": detail.id,
                "name": detail.name,
                # "study_project_id": detail.study_project.id,
                "study_project_name": detail.study_project.name,
                "score": detail.score,
                "c_date": detail.c_date.strftime("%Y-%m-%d"),
                "c_time": detail.c_time.strftime("%Y-%m-%d %H:%M:%S"),
                "notes": detail.notes or "",
                # "creator": detail.creator
            })

        return JsonResponse({
            "errno": "0",
            "errmsg": "",
            "data": {
                "total": total_count,
                "page": page,
                "page_size": page_size,
                "items": data
            }
        })

    except Exception as e:
        logger.error(f"获取学习项目明细列表失败: {str(e)}", exc_info=True)
        return JsonResponse({
            "errno": "1",
            "errmsg": "系统错误，请联系管理员"
        })