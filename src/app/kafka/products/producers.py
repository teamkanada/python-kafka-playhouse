import json

from .messages import get_product_fit_vote_message


def produce_product_fit_vote(topic, **kwargs):
    with topic.get_sync_producer(serializer=lambda x: json.dumps(x)) as producer:
        message = get_product_fit_vote_message(kwargs)
        if message:
            producer.produce(message)
