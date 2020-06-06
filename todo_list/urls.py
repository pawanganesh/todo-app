from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('edit/<int:id>/', views.edit_task, name="edit_task"),
    path('delete/<int:id>/', views.delete_task, name="delete_task"),
    path('cross_off/<int:id>/', views.cross_off, name="cross_off"),
    path('uncross/<int:id>/', views.uncross, name="uncross")
]