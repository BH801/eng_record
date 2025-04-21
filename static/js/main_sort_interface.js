      document.getElementById("submitBtn").addEventListener("click", function () {
    const name = document.getElementById("name").value;
    const note = document.getElementById("note").value;

    // 获取 CSRF 令牌
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    // 构建请求体
    const formData = new FormData();
    formData.append("name", name);
    formData.append("note", note);

    // 发送POST请求
    fetch("http://127.0.0.1:8000/main_sort", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": csrfToken // 添加 CSRF 令牌到头部
        },
        credentials: "include", // 确保发送附带的 Cookie
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("网络错误或 CSRF 验证失败");
            }
            return response.json();
        })
        .then((data) => {
            document.getElementById("message").textContent = data.message;
        })
        .catch((error) => {
            console.error("Error:", error);
            document.getElementById("message").textContent = "添加失败，请重试！";
        });
});