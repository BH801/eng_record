TASK_CYCLE_CHOICES = {
    # {0: '每天', 1: '每周'}
    0: '每天',
    1: '每周',
}

STATUS_CHOICES = {
    # {0: '子任务汇总', 1: '单词状态记录'
    0: '子任务汇总',
    1: '单词状态记录',
}

# 认识与否状态：
WORD_STATUS_CHOICES = {
    0: '未认识',
    1: '认识',
}

# 这个时间间隔内的才计算总时长
DURATION_INTERVAL = 90

# redis中存储的任务状态的key模板：
TASK_STATUS_KEY = 'user:{user_id}:task:{task_id}:status'
# 用户”已掌握“的单词id集合的key模板：
USER_MEMORIZED_WORDS_KEY = 'user:{user_id}:memorized_words'
# 用户每个task的”已掌握"的key的模板
USER_TASK_MEMORIZED_WORDS_KEY = 'user:{user_id}:task:{task_id}:memorized_words'

# 存储用户的所有Logs到Redis
USER_ALL_LOGS_KEY = 'user_{user_id}_all_logs'

# register IP limit ip 日注册量限制
REGISTER_IP_LIMIT = 10

# 用户量上限
USER_LIMIT = 20000

# 分类列表的key
CATEGORY_LIST_KEY = 'category_list'
# 分类id的key 包含单词数量
CATEGORY_ID_KEY = 'category:{category_id}'

# 子任务缓存ID               redis_key = f'user:{user.id}:task:{task.id}:subtask:{sub_task.id}:words'  # 移动到配置文件中
SUBTASK_ID_CACHE_KEY = 'user:{user_id}:task:{task_id}:subtask:{subtask_id}:words'

# 用户所有任务上限：
USER_TASK_LIMIT = 100


# 分析数据限制最近XX天
ANALYSIS_LIMIT_DAYS = 90

NO_REVIEW_WORDSW_MES = '暂时没有需要复习的单词，请再接再厉'


# word_id to mean cache key
WORDID2MEAN_CACHE_KEY = 'word_id:{word_id}_mean'