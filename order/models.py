from django.db import models
from django.contrib.auth.models import User

class Kind(models.Model):
    kind = models.CharField(max_length=20)
    def __str__(self):
        return self.kind

class Order(models.Model):
    order_name = models.CharField(max_length=20)
    order_time = models.DateTimeField()
    def __str__(self):
        return self.order_name

class Project(models.Model):
    order_of_project = models.ForeignKey(Order, on_delete=models.CASCADE)
    project_index = models.CharField(max_length=20)
    project_kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    project_describtion = models.TextField()
    project_count = models.IntegerField(default=1)
    project_price = models.IntegerField(default=0)
    def __str__(self):
        return self.project_describtion

class Provider(models.Model):
    provider_name = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    provider_price = models.CharField(max_length=20)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    def __str__(self):
        return self.provider_name