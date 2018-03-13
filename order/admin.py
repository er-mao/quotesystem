from django.contrib import admin
from .models import Order, Project, Kind

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 10

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['order_name']}),
        ("日期", {'fields': ['order_time']}),
    ]
    inlines = [ProjectInline]
    
admin.site.register(Order, OrderAdmin)
admin.site.register(Kind)