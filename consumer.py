import pika

params = pika.URLParameters('amqps://fiqifbvt:IBf7SMmNWIdPrShKHawpnPrS6ogrFvSv@rattlesnake.rmq.cloudamqp.com/fiqifbvt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print("Started Consumming ")

channel.start_consuming()

channel.close()