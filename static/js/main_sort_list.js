$(document).ready(function() {
    // Load main sort data when page loads
    loadMainSortList();

    // Variable to store the ID to be deleted
    let deleteId = null;
    let deleteName = null;

    // Set up event delegation for delete buttons
    $('#main-sort-list').on('click', '.delete-btn', function() {
        deleteId = $(this).data('id');
        deleteName = $(this).data('name');
        $('#delete-sort-name').text(deleteName);
        $('#deleteConfirmModal').modal('show');
    });

    // Confirm delete button click handler
    $('#confirm-delete').click(function() {
        if (deleteId) {
            deleteMainSort(deleteId);
        }
    });
});

/**
 * Load the list of main categories
 */
function loadMainSortList() {
    $.ajax({
        url: 'main_sort',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            if (response && response.errno === "0") {
                displayMainSort(response.data);
            } else {
                console.error('无法获取主分类数据');
                $('#main-sort-list').html('<tr><td colspan="3" class="text-center">无法获取数据</td></tr>');
            }
        },
        error: function(xhr, status, error) {
            console.error('请求失败:', error);
            $('#main-sort-list').html('<tr><td colspan="3" class="text-center">获取数据失败</td></tr>');
        }
    });
}

/**
 * Display main sort data in the table
 * @param {Array} data - Array of main sort objects
 */
function displayMainSort(data) {
    let html = '';

    if (data && data.length > 0) {
        data.forEach(function(item) {
            html += `<tr>
                <td>${item.id}</td>
                <td>${item.name}</td>
                <td>
                    <a href="edit_main_sort.html?id=${item.id}" class="btn btn-sm btn-info mr-3">编辑</a>
                    <button class="btn btn-sm btn-danger delete-btn" data-id="${item.id}" data-name="${item.name}">删除</button>
                </td>
            </tr>`;
        });
    } else {
        html = '<tr><td colspan="3" class="text-center">暂无数据</td></tr>';
    }

    $('#main-sort-list').html(html);
}

/**
 * Delete a main sort category
 * @param {number} id - ID of the category to delete
 */
function deleteMainSort(id) {
    // 获取CSRF token
    const csrftoken = getCookie('csrftoken');

    $.ajax({
        url: '/main_sort',
        type: 'DELETE',
        // 在请求头中添加CSRF token
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        data: JSON.stringify({
            id: id
        }),
        contentType: 'application/json',
        success: function(response) {
            // 关闭弹窗
            $('#deleteConfirmModal').modal('hide');

            if (response && response.errno === "0") {
                alert('删除成功');
                // 重新加载数据
                loadMainSortList();
            } else {
                alert(response.errmsg || '删除失败，请重试');
            }
        },
        error: function(xhr, status, error) {
            console.error('删除请求失败:', error, xhr.responseText);
            alert('删除请求失败 (' + xhr.status + '): ' + error);
            $('#deleteConfirmModal').modal('hide');
        }
    });
}

// 修正的获取cookie函数
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}