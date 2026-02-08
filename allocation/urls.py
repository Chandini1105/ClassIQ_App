from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('book/', views.book_classroom, name='book_classroom'),
    path('active-classes/', views.active_classes, name='active_classes'),
    path('help/', views.help, name='help'),
    path('admin/add-user/', views.add_user, name='add_user'),
]
