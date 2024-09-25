"""
URL configuration for unveil project.

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

from apps.core.urls import router as core_router
from apps.users.urls import router as users_router
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(csrf=True)

api.add_router("", core_router)
api.add_router("", users_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
]
