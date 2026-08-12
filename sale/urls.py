from django.urls import path
from sale.views import AddCartItemView, CartDetailView, SubmitPaymentView

urlpatterns = [
    path('add-cart-item/', AddCartItemView.as_view(), name='add-cart-item'),
    path('cart-detail/', CartDetailView.as_view(), name='cart-detail'),
    path('submit-payment/', SubmitPaymentView.as_view(), name='submit-payment'),
]
