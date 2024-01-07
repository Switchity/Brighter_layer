
from django.contrib import admin
from django.urls import path
from Linux import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('p1/', views.index),
    path('p2/', views.index)
]
