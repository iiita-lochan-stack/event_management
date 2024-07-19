from django.urls import path
from .views import payment_view, payment_success_view

urlpatterns = [
   path('payment/', payment_view, name='payment'),
   path('payment/success/', payment_success_view, name='payment_success'),
]