"""
URL configuration for skillsmatrix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# skillsmatrix/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # login URL
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # logout URL
    path('signup/', views.signup, name='signup'),  # signup URL
    path('dashboard/', views.dashboard, name='dashboard'),  # dashboard URL
    path('', views.home, name='home'),  # home view
    path('signup/<str:tier>/', views.signup, name='signup'),
    path('select-tier/', views.select_tier, name='select_tier'),

]

