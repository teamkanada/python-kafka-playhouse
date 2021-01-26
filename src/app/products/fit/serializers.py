from .models import ProductFit
from rest_framework import routers, serializers, viewsets


class ProductFitSerializer(serializers.Serializer):
    class Meta:
        model = ProductFit
        fields = '__all__'
