from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gallery_view, name='gallery_view'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='gallery_view'), name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create-category/', views.create_category, name='create_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 