from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="owner-home"),
    path('post-complaints/', views.post_complaints, name='post-complaints'),
    path('make-payment/', views.make_payment, name='make-payment'),
    path('ledger/', views.ledger, name='owner-ledger'),
]

