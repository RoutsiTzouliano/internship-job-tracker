from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.registration, name='candidate_register'),

    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='candidate_login'
    ),

    path(
        'logout/',
        LogoutView.as_view(next_page='job_list'),
        name='candidate_logout'
    ),
]