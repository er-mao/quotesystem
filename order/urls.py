from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as order_views

urlpatterns = [
    path('', order_views.order, name='order'),
    path('<int:order_number>', order_views.order_number, name='order_number'),
    path('my_order/', order_views.my_order, name='my_order'),
]