from rest_framework import routers
from .viewsets import VerticalViewSet


router = routers.DefaultRouter()
router.register(r'verticals', VerticalViewSet)
