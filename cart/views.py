# File: cart/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncreaseProductQuantity(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, cart_item_id):
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart_item.quantity += 1
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)


class ViewCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)


class RemoveFromCart(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
        try:
            cart_item = CartItem.objects.get(pk=cart_item_id, user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response("Cart item not found.", status=status.HTTP_404_NOT_FOUND)


class ApplyDiscount(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Add logic to apply discounts or promo codes
        return Response("Discount applied successfully.", status=status.HTTP_200_OK)


class SaveForLater(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, cart_item_id):
        # Add logic to move item to "saved for later" list
        return Response("Item saved for later.", status=status.HTTP_200_OK)


class PersistentCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Add logic to retrieve persistent cart items (if any)
        return Response("Persistent cart retrieved successfully.", status=status.HTTP_200_OK)
