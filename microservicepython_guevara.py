#!/usr/bin/python
#pip install mysqlclient
#pythonmicroservice.c7v0hpe7htge.us-east-2.rds.amazonaws.com
import pika
import MySQLdb
import json


class Microservice:
    
    @staticmethod
    def microserviceLogic ():

        try:
            db = MySQLdb.connect(host="localhosttestnoip", user="root", passwd="Guevara_Ardila", db="prueba_arquitecturas_agiles")        
            cur = db.cursor()

            cur.execute("SELECT * FROM persona")

            for row in cur.fetchall():
                print (json.dumps(row, indent=4, sort_keys=True, default=str))
            db.close()

        except IOError as e:

            print ("Error BD: ".format(e.errno, e.strerror))

    @staticmethod
    def queuePublishMessage ():
        try:

            credentials = pika.PlainCredentials('test', 'test')
            parameters = pika.ConnectionParameters('192.168.56.7',5672,'/',credentials)
            connection = pika.BlockingConnection(parameters)

            channel = connection.channel()
            channel.queue_declare(queue='micro_sv')
            channel.basic_publish(exchange='',routing_key='micro_sv',body='Hello World!')
            print(" [x] Sent 'Hello World!'")
            connection.close()


        except IOError as e:
            print ("Error Queue: ".format(e.errno, e.strerror))

        

Microservice.microserviceLogic()
Microservice.queuePublishMessage()

   

