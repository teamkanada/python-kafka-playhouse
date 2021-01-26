from .models import Product
from rest_framework import routers, serializers, viewsets


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
