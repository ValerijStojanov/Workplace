
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('detail-pozice/<slug>/', views.detail_pozice, name='detail_pozice'),
    path('vytvorit_pracovni_pozici/', views.vytvorit_pracovni_pozici, name='vytvorit_pracovni_pozici'),
    path('succeses_page_form', views.succeses_page_form, name='succeses_page_form'),
    path('registrovat/', views.register, name='register'),
    path('prihlasit/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),   
]
