from apploja.models import Order, Product
from apploja.serializers import OrderSerializer, ProductSerializer
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     GenericAPIView)
from rest_framework.response import Response
from rest_framework import renderers


class OrderList(ListCreateAPIView):
    """
    List all Orders, or create a new Order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Order instance.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDesc(GenericAPIView):
    """
    Retrieve Order description
    """
    queryset = Order.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        order = self.get_object()
        return Response(order.description)


class ProductList(ListCreateAPIView):
    """
    List all Product, or create a new Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Product instance.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDesc(GenericAPIView):
    """
    Retrieve Product description
    """
    queryset = Product.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(product.description)
