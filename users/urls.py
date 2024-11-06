from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/credit_report', views.credit_report, name='credit_report'),
    path('dashboard/disputes', views.disputes, name='disputes'),
    path('dashboard/setting', views.setting, name='setting'),

]