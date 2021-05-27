#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Receive_information', durable=False)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

while True:
    #channel.basic_qos(prefetch_count=1000)
    channel.basic_consume(queue='Receive_information', on_message_callback=callback)
    channel.start_consuming()
    time.time(1000)
    clc
