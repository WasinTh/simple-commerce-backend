from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from sale.serializers import AddCartItemSerializer, CartDetailSerializer, SubmitPaymentSerializer
from sale.models import Cart, OrderItem

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

    def __generate_order_items(self, order):
        for item in order.cart.items.all():
            OrderItem.objects.create(
                order=order, 
                product=item.product, 
                quantity=item.quantity, 
                price=item.product.price * item.quantity
            )

    def __clean_cart(self, cart):
        cart.items.all().delete()

    def perform_create(self, serializer):
        order = serializer.save(
            cart=self.request.user.member.cart,
            total_price=self.request.user.member.cart.total_price
        )
        self.__generate_order_items(order)
        self.__clean_cart(self.request.user.member.cart)

