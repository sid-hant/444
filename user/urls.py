from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import signup

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="user-login.html", redirect_authenticated_user=True), name='user-login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(),login_url='user:user-login'), name='user-logout'),
    path('sign-up/', signup, name='user-sign-up'),
    
]