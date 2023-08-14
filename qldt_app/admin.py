from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from qldt_app.models import nguoiDung

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(nguoiDung,UserModel)