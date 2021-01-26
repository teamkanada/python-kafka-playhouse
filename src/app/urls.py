from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from .verticals.viewsets import VerticalViewSet
from .products.viewsets import ProductViewSet
from .products.fit.viewsets import ProductFitViewSet


router = routers.SimpleRouter()
router.register(r'verticals', VerticalViewSet)
router.register(r'products', ProductViewSet)

domains_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
domains_router.register(r'fit', ProductFitViewSet, basename='product-fit')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(domains_router.urls)),
]
