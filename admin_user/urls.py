from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet

router = DefaultRouter()
router.register('admin-users', AdminUserViewSet)
from . import views

app_name = 'admin_user'


urlpatterns = [
    path('auth/login', views.LoginView.as_view(), name='login'),
    path('auth/logout', views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]


