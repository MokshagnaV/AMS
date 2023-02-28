from django.urls import path
from . import views
urlpatterns = [
    path('', views.index.as_view(), name="association-home"),
    path('notice_add/', views.notice_add.as_view(), name="notices_add"),
    path('complaints/', views.complaints.as_view(), name='complaints'),
    path('ledger/', views.ledger.as_view(), name='ledger'),
    path('ledger/add', views.addexpense.as_view(), name='addexpense'),
    
]
