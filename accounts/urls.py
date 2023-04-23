from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.showLogin, name='show'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_user, name='logout'),
]