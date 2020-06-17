from django.db import models

# Create your models here.

class Test(models.Model):
    
    name = models.CharField(max_length=200, verbose_name="用例名称")
    url = models.CharField(max_length=200, verbose_name='项目URL')
    status = models.ImageField(default=0, verbose_name='测试状态')



