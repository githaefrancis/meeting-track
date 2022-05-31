from django.contrib import admin
from .models import TaskBlock, CustomUser,UserCustom,Task,SubTask,Priority
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Priority)
admin.site.register(TaskBlock)
