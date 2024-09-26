from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('transaction-test/', views.transaction_test, name='transaction_test'),
]