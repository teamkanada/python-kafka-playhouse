import json
from django.conf import settings
from pykafka import KafkaClient, SslConfig

kafka_settings = settings.KAFKA
config = None
product_producer = None


def json_serializer(message, partition_key):
    return json.dumps(message).encode('utf-8'), partition_key


if kafka_settings.get('SSL', None):
    ssl_settings = kafka_settings['SSL']
    config = SslConfig(
        cafile=ssl_settings['CAFILE'],
        certfile = ssl_settings.get('CERTFILE', None),
        keyfile = ssl_settings.get('KEYFILE', None),
        password = ssl_settings.get('PASSWORD', None)
    )

client = KafkaClient(hosts=",".join(kafka_settings['HOSTS']), ssl_config=config)

if client.topics:
    product_topic = client.topics['product']
    product_producer = product_topic.get_producer(serializer=json_serializer, min_queued_messages=1, linger_ms=0)