from django.urls import path
from . import views

urlpatterns = [


	path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),




	

    path('', views.store, name="store"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete"),
]