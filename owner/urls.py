from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="owner-home"),
    path('login/', views.login, name="login"),
    path('post-complaints/', views.post_complaints, name='post-complaints'),
    path('ledger/', views.ledger, name='owner-ledger'),
]

