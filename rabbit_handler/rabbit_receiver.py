import json
import os

import pika as pika

credentials = pika.PlainCredentials(os.environ.get('RABBITMQ_DEFAULT_USER'), os.environ.get('RABBITMQ_DEFAULT_PASS'))
rabbit_host = os.environ.get('RABBIT_HOST')


def callback(ch, method, properties, body: bytes):
    # print(body.decode())
    received = json.loads(body.decode('utf-8'))
    # print(method.routing_key)
    match method.routing_key:
        case "core-test-control":
            print("Queue 1")
            # message_processing.process_test_control(received)
        case "core-data":
            print(received)
            # message_processing.process_data(received)


def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_host, 5672, '/', credentials))
    channel = connection.channel()
    queues = ['core-test-control']
    for queue in queues:
        channel.queue_declare(queue=queue)
        channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=callback)
    channel.start_consuming()
    print(' [*] Waiting for messages. To exit press CTRL+C')
