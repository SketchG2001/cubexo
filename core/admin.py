from django.contrib import admin
from .models import Course,Student,Teacher
from django.db import connection


class TenantAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj =None):
        if connection.schema_name == 'public':
            return False
        return super().has_view_permission(request, obj)
admin.site.register(Course,TenantAdmin)
admin.site.register(Student,TenantAdmin)
admin.site.register(Teacher,TenantAdmin)
