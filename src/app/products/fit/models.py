import logging
from django.db import models
from .constants import FIT_SCALE

logger = logging.getLogger(__name__)


class Vote(models.Model):
    """
    A Fit vote
    """
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    vote = models.PositiveSmallIntegerField(choices=FIT_SCALE)
    # We probably need some kind of reference to the user to keep the data from being flooded
    # Leaving this out of the example to keep it simple - This should be unique constrained to the product
    # user_uuid = models.UUIDField()


class ProductFit(models.Model):
    """
    A summary of how a product fits
    """
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, unique=True)
    score = models.DecimalField(max_digits=3, decimal_places=2)
