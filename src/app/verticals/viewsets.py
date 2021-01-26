from .models import Vertical
from .serializers import VerticalSerializer
from rest_framework import viewsets


class VerticalViewSet(viewsets.ModelViewSet):
    queryset = Vertical.objects.all()
    serializer_class = VerticalSerializer
