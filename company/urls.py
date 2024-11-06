from django.urls import path
from . import views


app_name = 'company'
urlpatterns = [
    path('register/', views.register, name='company_register'),
    path('login/', views.company_login, name='company_login'),
    path('dashboard/', views.dashboard, name='company_dashboard'),
    # Add other URLs as needed
]
