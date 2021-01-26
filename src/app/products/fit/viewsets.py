from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from .models import ProductFit
from .serializers import ProductFitSerializer


class ProductFitViewSet(viewsets.ViewSet):
    queryset = ProductFit.objects.all()

    def list(self, request, product_pk=None):
        try:
            product_fit = self.queryset.get(product=product_pk)
            if product_fit:
                serializer = ProductFitSerializer(object)
                return Response(serializer.data)
        except ProductFit.DoesNotExist:
            return Response(None, status=404)

    def create(self, request, product_pk=None):
        pass


