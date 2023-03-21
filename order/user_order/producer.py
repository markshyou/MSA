import pika
import json

params = pika.URLParameters('amqps://xkiwqhmr:c1UHPadXstZU23g6xdB8B2BZiVlxGDEp@dingo.rmq.cloudamqp.com/xkiwqhmr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='boss', body=json.dumps(body), properties=properties)