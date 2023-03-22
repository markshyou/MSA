import pika
import json

params = pika.URLParameters('amqps://fwvhtkhf:i5nTBg4I3H6w-lQxEraNGTNQVDOsepDQ@dingo.rmq.cloudamqp.com/fwvhtkhf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='boss', body=json.dumps(body), properties=properties)