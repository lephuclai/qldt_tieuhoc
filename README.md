# Quản lý đào tạo trường tiểu học

# 1. Cài đặt

- MySQL và MySQL Workbench
- Django
- Thư viện Python cần cài đặt: pymysql
- Sửa lỗi khi chạy makemigrations (trên Linux)
    - `pip install --upgrade setuptools`
    - `pip install pymysql`
    - Trong file [init.py](http://init.py) (cùng thư mục với settings.py):
        
        ```python
        import pymysql
        pymysql.install_as_MySQLdb()
        ```
        

# 2. Tạo cơ sở dữ liệu:

Cơ sở dữ liệu cần phải đặt các thông tin như sau:

- database name: qldt
- user: qldt
- password: qldt123L!

# 3. Tạo các bảng trong cơ sở dữ liệu

Chạy các lệnh sau ở terminal:

- `python manage.py makemigrations qldt_app`
- `python manage.py migrate`

# 4. Tạo tài khoản admin:

Chạy lệnh sau để tạo tài khoản admin: `python manage.py createsuperuser`

Sau đó thực hiện nhập email và mật khẩu ở trên terminal

# 5. Chạy server cho webapp:

Chạy lệnh sau ở terminal: `python manage.py runserver localhost:8000`

Có thể đổi cổng 8000 thành cổng khác tùy thuộc vào mục đích