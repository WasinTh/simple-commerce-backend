from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from sale.serializers import AddCartItemSerializer, CartDetailSerializer, SubmitPaymentSerializer
from sale.models import Cart


class AddCartItemView(generics.CreateAPIView):
    serializer_class = AddCartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.member.cart)


class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.member.cart


class SubmitPaymentView(generics.CreateAPIView):
    serializer_class = SubmitPaymentSerializer
    permission_classes = [IsAuthenticated]

