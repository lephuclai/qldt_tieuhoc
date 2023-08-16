# qldt_tieuhoc

1. Tao database mysql:
Tuy thuoc vao he dieu hanh moi nguoi tim cach tao database theo huong dan o tren mang. Chu y:
- database name: qldt
- user: qldt
- password: qldt123L!

2. Tao cac bang
Mo terminal o trong code editor/IDE va chay cac lenh (doi voi Linux):
- ` python manage.py makemigrations qldt_app `
- ` python manage.py migrate `

3. Tao tai khoan admin
Mo terminal o trong code editor/IDE va chay cac lenh (doi voi Linux):
- ` python manage.py createsuperuser `

4. Chay server cho webapp
- ` python manage.py runserver localhost:8000 `