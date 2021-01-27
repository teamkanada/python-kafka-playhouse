from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from app.kafka.clients import get_topic
from app.kafka.constants import PRODUCT_TOPIC
from app.kafka.products.producers import produce_product_fit_vote
from .models import ProductFit
from .serializers import ProductFitSerializer, VoteSerializer


class ProductFitViewSet(viewsets.ViewSet):
    queryset = ProductFit.objects.all()

    def list(self, request, product_pk=None):
        try:
            product_fit = self.queryset.get(product=product_pk)
            serializer = ProductFitSerializer(product_fit)
            return Response(serializer.data)
        except ProductFit.DoesNotExist:
            return Response(None, status=404)

    def create(self, request, product_pk=None):
        if product_pk is None:
            raise Http404('Product not found')
        data = dict(request.data)
        data['product'] = product_pk
        serializer = VoteSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            topic = get_topic(PRODUCT_TOPIC)
            produce_product_fit_vote(topic, serializer)
            return Response({}, status=201)