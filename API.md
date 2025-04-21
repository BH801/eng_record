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


## 学习项目管理API
http://127.0.0.1:8000/study_project


##  学习项目添加页面地址：
http://127.0.0.1:8000/study_project_page
## 学习项目列表页面地址：
http://127.0.0.1:8000/study_project_page_list


