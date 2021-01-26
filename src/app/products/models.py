import logging
import uuid
from django.db import models


logger = logging.getLogger(__name__)


class Product(models.Model):
    """
    A Category for a given product
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    vertical = models.ForeignKey('verticals.Vertical', on_delete=models.CASCADE)
