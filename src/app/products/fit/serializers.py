from rest_framework import routers, serializers, viewsets
from .models import ProductFit, Vote
from .constants import VERY_SMALL, VERY_BIG


class VoteSerializer(serializers.Serializer):
    product = serializers.UUIDField()
    vote = serializers.IntegerField(min_value=VERY_SMALL, max_value=VERY_BIG)


class ProductFitSerializer(serializers.Serializer):
    class Meta:
        model = ProductFit
        fields = '__all__'
