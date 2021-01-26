from typing import List, Set, Dict, Union
import logging
from django.db import models


logger = logging.getLogger(__name__)


class Vertical(models.Model):
    """
    A Category for a given product
    """
    slug = models.CharField(primary_key=True, null=False, blank=False, max_length=30, verbose_name="slug")
    name = models.CharField(max_length=255)
