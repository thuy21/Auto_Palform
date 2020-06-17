from django.contrib import admin
from .models import Test
# Register your models here.

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'status']


admin.site.site_header = "LECENT自动化测试平台"