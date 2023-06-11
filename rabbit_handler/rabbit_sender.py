import json
import os

import pika as pika

credentials = pika.PlainCredentials(os.environ.get('RABBITMQ_DEFAULT_USER'), os.environ.get('RABBITMQ_DEFAULT_PASS'))
rabbit_host = os.environ.get('RABBIT_HOST')


def produce(queue, message_body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_host, 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(
        exchange='',
        body=json.dumps(message_body).encode('utf-8'),
        routing_key=queue
    )
    channel.close()
    connection.close()
