import json

from ..clients import product_producer
from .messages import get_product_fit_vote_message


def produce_product_fit_vote(data):
    message = get_product_fit_vote_message(data)
    if message:
        product_producer.produce(message)
