import json
import os
import redis
from loguru import logger
from plan.models import SubTask,Task
from django.core.cache import caches

#   设定每周记录，记录所有等级，100mb分割
logger = logger.bind(name = 'logger')
logger.add("logs/week_{time:YYYY-MM-DD}.log", rotation="1 week", retention="7 days", level="DEBUG", enqueue=True, encoding="utf-8", compression="zip", backtrace=True, diagnose=True)

redis_client = redis.Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')),
                           db=int(os.getenv('REDIS_DB')), password=os.getenv('REDIS_PASSWORD'))

redis_client_decode = redis.Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')),
                           db=int(os.getenv('REDIS_DB')), password=os.getenv('REDIS_PASSWORD'), decode_responses=True)


cache_conn  = caches['default']
# 将xdf的单词列表合并为字符串
def combine_mean(text):
    if not text:
        text = '暂无释义'
    # print('aaa')
    # print(text)
    result = ''
    try:
        js = json.loads(text)
        for i in js:
            print(i)
            result =result + i.get('prop','') + ' ' + '；'.join(i.get('means',[])) + '\n'
    except:
        return text + ' '
    # print(result,'xxx')
    return result

# 通过task查last subtask 带缓存
def task2lastsubtask(task_id,fresh = False):
    cache_key = f'task2lastsubtask_{task_id}'
    last_subtask = cache_conn.get(cache_key)
    if last_subtask and  not fresh:
        return last_subtask
    else:
        subtask=SubTask.objects.filter(task_id=task_id).order_by('-create_time').first()
        if not subtask:
            # 根据任务类型创建

            from plan.management.commands.review_store_tasks_in_redis import generate_review_subtasks_and_store_in_redis
            from plan.management.commands.store_tasks_in_redis import generate_subtasks_and_store_in_redis
            try:
                task = Task.objects.get(id=task_id)
            except:
                logger.info(f'未找到任务，task_id:{task_id}')
                return None
            logger.info(f'未找到子任务，生成新的subtask,task_id:{task_id}')
            if task.review_source:
                generate_review_subtasks_and_store_in_redis(task)
            else:
                generate_subtasks_and_store_in_redis(task)
            return task2lastsubtask(task_id)
        cache_conn.set(cache_key,subtask.id,timeout=60*60*24*7)
        return subtask.id

from utils.r_cache import get_word_from_cache
# 通过redis获取最尾部的N个单词的信息
def get_tail_words(redis_key):
    # redis_key = SUBTASK_ID_CACHE_KEY.format(user_id=user.id, task_id=task.id, subtask_id=sub_task.id)
    # 获取尾部的单词id
    word_ids = redis_client.lrange(redis_key, -10, -1)
    # 反转数组
    # word_ids = word_ids[::-1]
    res = []
    for i in word_ids:
        word_id = int(i)
        word = get_word_from_cache(word_id)
        res.append({'id':word.id,'word':word.word_spelling,'mean':combine_mean(word.word_meaning)})
    return res


def is_vip(user_id):
    res = {'is_vip': True,
           'expire_date': '2025-06-31'}
    if user_id in [1,'1']:
        res = {'is_vip':True,
               'expire_date':'2025-12-31'}
        return res
        # return True
    else:
        return res
def is_super(user_id):
    if user_id in [1,'1',10]:
    # if user_id in [1, '1' ]:
        res = {'is_super':True}
        return res
    else:
        return {}

import ipaddress

def get_client_ip(request) -> str:
    """获取客户端真实IP"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '')

    # 验证IP地址的有效性
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        return '0.0.0.0'

def id2audio(word_id,sort='en'):
    url = '//www.wordrun.cn/media/audio/word_audio_{}_{}.mp3'
    # logger.info(word_id,sort)
    logger.info(f'获取音频，word_id:{word_id},type word_id:{type(word_id)}')
    try:
        if sort == 'us':
            return url.format('us',int(word_id))
        else:
            return url.format('en', int(word_id))
    except Exception as e:
        logger.error(f'获取音频失败，word_id:{word_id},type word_id:{type(word_id)},Exception:{e}')