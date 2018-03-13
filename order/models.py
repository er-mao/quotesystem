from django.db import models
from django.contrib.auth.models import User

class Kind(models.Model):
    kind = models.CharField(max_length=20, verbose_name="种类")
    def __str__(self):
        return self.kind
    class Meta:
        verbose_name = "项目种类"
        verbose_name_plural = "项目种类"

class Order(models.Model):
    order_name = models.CharField(max_length=20, verbose_name="订单名称")
    order_time = models.DateTimeField(verbose_name="订单时间")
    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"

class Project(models.Model):
    order_of_project = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="所属项目")
    project_index = models.CharField(max_length=20, verbose_name="项目编号")
    project_kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name="项目种类")
    project_describtion = models.TextField(verbose_name="项目描述")
    project_count = models.IntegerField(default=1, verbose_name="所需数目")
    project_price = models.IntegerField(default=0, verbose_name="报价")
    def __str__(self):
        return self.project_describtion
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"

class Provider(models.Model):
    provider_name = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    provider_price = models.CharField(max_length=20)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    def __str__(self):
        return self.provider_name
    class Meta:
        verbose_name = "供应商报价"
        verbose_name_plural = "供应商报价"