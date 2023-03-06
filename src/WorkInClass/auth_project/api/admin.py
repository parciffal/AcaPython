from django.contrib import admin
from django.utils.html import mark_safe

from .models import UserModel, TodoModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user','verify_code', 'get_todos']

    def get_todos(self, obj):
        link = "/admin/auth/user/{}/change/".format(obj.user.id)
        kil = """<a href="{}">{}</a>""".format(link, obj.user.get_username())
        return mark_safe(kil)

    def get_user(self, obj: UserModel):
        link = "/admin/auth/user/{}/change/".format(obj.user.id)
        kil = """<a href="{}">{}</a>""".format(link, obj.user.get_username())
        return mark_safe(kil)


@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'is_active', 'get_user']

    def get_user(self, obj: TodoModel):
        link = "/admin/auth/user/{}/change/".format(obj.user.id)
        kil = """<a href="{}">{}</a>""".format(link, obj.user.get_username())
        return mark_safe(kil)


