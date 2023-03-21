import pika
import os, django, json

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'order.settings')
django.setup()

from user_order.models import Order,Shop


params = pika.URLParameters('amqps://xkiwqhmr:c1UHPadXstZU23g6xdB8B2BZiVlxGDEp@dingo.rmq.cloudamqp.com/xkiwqhmr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    id = json.loads(body)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()