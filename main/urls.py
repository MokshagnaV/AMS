from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="main"),
    path('own-log', views.owner_login, name="owner-login"),
    path('ass-log', views.association_login, name="association-login"),
    path('login', views.login, name="main-login"),
    path('signup', views.signup, name="main-signup"),
    path("logout", views.logoutUser, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/reset.html"),
         name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/reset_done.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/reset_complete.html"),
         name="password_reset_complete"),

]
