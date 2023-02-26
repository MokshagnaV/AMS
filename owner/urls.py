from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="home"),
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.login.as_view(), name="login"),
    path('post-complaints/', views.post_complaints.as_view(), name='post-complaints'),
    path('ledger/', views.ledger.as_view(), name='owner-ledger'),
]

