$(document).ready(function() {
    // 初始化日期选择器
// Flatpickr 配置
flatpickr("#c_date", {
    enableTime: true, // 启用时间选择
    dateFormat: "Y-m-d H:i", // 设置日期时间格式
    locale: "zh", // 使用中文
    minuteIncrement: 1, // 分钟增量为1
    time_24hr: true, // 使用24小时制
    defaultHour: new Date().getHours(), // 默认当前小时
    defaultMinute: new Date().getMinutes(), // 默认当前分钟
});

    // 加载学习项目下拉列表
    $.ajax({
        url: '/study_project',
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
        error: function(xhr, status, error) {
            Swal.fire({
                title: '错误',
                text: '加载学习项目列表失败: ' + error,
                icon: 'error'
            });
        },
        success: function(response) {
            if (response.errno === "0") {
                const select = $('#study_project');
                response.data.forEach(project => {
                    select.append(`<option value="${project.id}">${project.name}</option>`);
                });
            } else {
                Swal.fire({
                    title: '错误',
                    text: response.errmsg || '加载学习项目列表失败',
                    icon: 'error'
                });
            }
        }
    });

    // 表单提交处理
    $('#projectDetailForm').on('submit', function(e) {
        e.preventDefault();

        const formData = {
            name: $('#name').val(),
            study_project: $('#study_project').val(),
            score: $('#score').val(),
            c_datetime: $('#c_date').val(),
            notes: $('#notes').val()
        };

        $.ajax({
            url: '/api/project_detail/add',
            method: 'POST',
            data: JSON.stringify(formData),
            headers: {
                'Accept': 'application/json'
            },
            error: function(xhr, status, error) {
                Swal.fire({
                    title: '错误',
                    text: '提交失败: ' + error,
                    icon: 'error'
                });
            },
            success: function(response) {
                if (response.errno === "0") {
                    Swal.fire({
                        title: '成功',
                        text: '学习项目明细添加成功',
                        icon: 'success'
                    }).then(() => {
                        window.location.href = '/project_detail_list';
                    });
                } else {
                    Swal.fire({
                        title: '错误',
                        text: response.errmsg || '添加失败',
                        icon: 'error'
                    });
                }
            }
        });
    });
});