from django.conf import settings
from pykafka import KafkaClient, SslConfig


def get_client():
    kafka_settings = settings.KAFKA
    config = None
    if kafka_settings.get('SSL', None):
        ssl_settings = kafka_settings['SSL']
        config = SslConfig(
            cafile=ssl_settings['CAFILE'],
            certfile = ssl_settings.get('CERTFILE', None),
            keyfile = ssl_settings.get('KEYFILE', None),
            password = ssl_settings.get('PASSWORD', None)
        )
    return KafkaClient(hosts=",".join(kafka_settings['HOSTS']), ssl_config=config)


def get_topic(name, client=None):
    if client is None:
        client = get_client()
    return client[name]
