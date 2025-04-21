$(document).ready(function() {
    let currentPage = 1;
    const pageSize = 10;

    function loadData(page = 1, searchName = '') {
        $.ajax({
            url: '/api/project_detail/list',
            method: 'GET',
            data: {
                page: page,
                page_size: pageSize,
                search_name: searchName
            },
            success: function(response) {
                if (response.errno === "0") {
                    renderTable(response.data.items);
                    renderPagination(response.data.total, response.data.page);
                    updatePageInfo(response.data.total, response.data.page, pageSize);
                } else {
                    showError('加载数据失败：' + response.errmsg);
                }
            },
            error: function(xhr, status, error) {
                showError('系统错误：' + error);
            }
        });
    }

    function renderTable(items) {
        const tbody = $('#detailTable tbody');
        tbody.empty();

        items.forEach(item => {
            const row = `
                <tr>
                    <td>${item.id}</td>
                    <td>${item.name}</td>
                    <td>${item.study_project_name}</td>
                    <td>${item.score}</td>
                    <td>${item.c_date}</td>
                    <td>${item.c_time}</td>
                    <td class="note-cell">
                        <a href="#" class="show-notes" data-notes="${encodeURIComponent(item.notes)}">
                            ${item.notes || '无'}
                        </a>
                    </td>
                    <td>
                        <button class="btn btn-sm btn-primary edit-btn" data-id="${item.id}">
                            <i class="fas fa-edit"></i> 编辑
                        </button>
                    </td>
                </tr>
            `;
            tbody.append(row);
        });
    }

    function renderPagination(total, currentPage) {
        const totalPages = Math.ceil(total / pageSize);
        const pagination = $('#pagination');
        pagination.empty();

        // 上一页
        pagination.append(`
            <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
                <a class="page-link" href="#" data-page="${currentPage - 1}">上一页</a>
            </li>
        `);

        // 页码
        for (let i = 1; i <= totalPages; i++) {
            if (
                i === 1 || // 第一页
                i === totalPages || // 最后一页
                (i >= currentPage - 2 && i <= currentPage + 2) // 当前页附近的页码
            ) {
                pagination.append(`
                    <li class="page-item ${i === currentPage ? 'active' : ''}">
                        <a class="page-link" href="#" data-page="${i}">${i}</a>
                    </li>
                `);
            } else if (
                i === currentPage - 3 || // 当前页前的省略号
                i === currentPage + 3 // 当前页后的省略号
            ) {
                pagination.append(`
                    <li class="page-item disabled">
                        <span class="page-link">...</span>
                    </li>
                `);
            }
        }

        // 下一页
        pagination.append(`
            <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
                <a class="page-link" href="#" data-page="${currentPage + 1}">下一页</a>
            </li>
        `);
    }

    function updatePageInfo(total, currentPage, pageSize) {
        const start = (currentPage - 1) * pageSize + 1;
        const end = Math.min(currentPage * pageSize, total);
        $('#pageInfo').text(
            `显示第 ${start} 到第 ${end} 条记录，共 ${total} 条记录`
        );
    }

    function showError(message) {
        Swal.fire({
            title: '错误',
            text: message,
            icon: 'error'
        });
    }

    // 事件处理
    $('#searchBtn').click(function() {
        const searchName = $('#searchName').val().trim();
        currentPage = 1;
        loadData(currentPage, searchName);
    });

    $('#searchName').keypress(function(e) {
        if (e.which === 13) {
            $('#searchBtn').click();
        }
    });

    $(document).on('click', '.page-link', function(e) {
        e.preventDefault();
        const page = $(this).data('page');
        if (page && !$(this).parent().hasClass('disabled')) {
            currentPage = page;
            const searchName = $('#searchName').val().trim();
            loadData(currentPage, searchName);
        }
    });

    $(document).on('click', '.show-notes', function(e) {
        e.preventDefault();
        const notes = decodeURIComponent($(this).data('notes'));
        $('#fullNotes').text(notes || '无备注');
        $('#notesModal').modal('show');
    });

    $(document).on('click', '.edit-btn', function() {
        const id = $(this).data('id');
        window.location.href = `/edit_project_detail?id=${id}`;
    });

    // 初始加载
    loadData();
});