# API





## records
helloword(is ok):
get:       http://127.0.0.1:8000/hello

主分类添加接口：
post:http://127.0.0.1:8000/main_sort
主分类获取接口：
get:http://127.0.0.1:8000/main_sort
响应值：
```json
{
    "errno": "0",
    "errmsg": "",
    "data": [
        {
            "id": 4,
            "name": "\u5199\u4f5c"
        },
        {
            "id": 3,
            "name": "\u53e3\u8bed"
        },
        {
            "id": 5,
            "name": "\u53e3\u8bedi"
        },
        {
            "id": 1,
            "name": "\u542c\u529b"
        },
        {
            "id": 2,
            "name": "\u9605\u8bfb"
        }
    ]
} 
```



## 主分类添加页面：
http://127.0.0.1:8000/main_sort_page
主分类列表页面：
http://127.0.0.1:8000/main_sort_page_list





##  学习项目添加页面地址：
http://127.0.0.1:8000/study_project_page
## 学习项目列表页面地址：
http://127.0.0.1:8000/study_project_page_list



## 学习项目管理API
http://127.0.0.1:8000/study_project
响应值：
```json
{
    "errno": "0",
    "errmsg": "",
    "data": [
        {
            "id": 2,
            "name": "\u525111 Test1 \u9605\u8bfb",
            "notes": "",
            "create_time": "2025-04-21T16:34:17.738Z"
        }
    ]
}
```


## 学习项目明细添加和列表页面
http://127.0.0.1:8000/project_detail_list
http://127.0.0.1:8000/project_detail_page






## 学习项目明细API相应列表：
```json
{
    "errno": "0",
    "errmsg": "",
    "data": {
        "total": 3,
        "page": 1,
        "page_size": 10,
        "items": [
            {
                "id": 3,
                "name": "\u6d4b\u8bd5",
                "study_project_name": "\u525111 Test1 \u9605\u8bfb",
                "score": 22,
                "c_date": "2025-04-22",
                "c_time": "2025-04-21 17:09:24",
                "notes": "\u6240\u4ea7\u751f\u7684\u4ecen"
            },
            {
                "id": 2,
                "name": "\u525111 \u7b2c\u4e00\u6b21",
                "study_project_name": "\u525111 Test1 \u9605\u8bfb",
                "score": 22,
                "c_date": "2025-04-22",
                "c_time": "2025-04-21 17:08:07",
                "notes": "\u9876\u9876\u9876"
            },
            {
                "id": 1,
                "name": "\u7b2c\u4e00\u6b21\u9605\u8bfb",
                "study_project_name": "\u525111 Test1 \u9605\u8bfb",
                "score": 80,
                "c_date": "2025-04-22",
                "c_time": "2025-04-21 17:03:47",
                "notes": "\u5bf93\u95195 \u517114"
            }
        ]
    }
}
```


