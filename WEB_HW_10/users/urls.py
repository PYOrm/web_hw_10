from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html", next_page="quotes:index"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
