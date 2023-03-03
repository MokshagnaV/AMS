from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="association-home"),
    path('notice_add/', views.notice_add, name="notices_add"),
    path('complaints/', views.complaints, name='complaints'),
    path('ledger/', views.ledger, name='association-ledger'),
    path('ledger/add', views.addexpense, name='addexpense'),
    path('payments', views.payments, name='payments'),
    path('complaint-resolve/<int:id>', views.complaint_resolve, name='complaint-resolve')
]
