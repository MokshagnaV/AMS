from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('own-log', views.owner_login, name="owner-login"),
    path('ass-log', views.association_login, name="association-login"),
    path('login', views.login, name="main-login"),
    path('signup', views.signup, name="main-signup"),
    path("logout",views.logoutUser, name="logout"),
] 