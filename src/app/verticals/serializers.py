from .models import Vertical
from rest_framework import serializers


class VerticalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vertical
        fields = ['slug', 'name']
