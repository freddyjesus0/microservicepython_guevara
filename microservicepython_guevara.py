#!/usr/bin/python
#pip install mysqlclient
#pythonmicroservice.c7v0hpe7htge.us-east-2.rds.amazonaws.com
import pika
import MySQLdb
import json
import requests
import sys
import asyncio
import aiohttp
from flask import Flask, request 

class Microservice:

    app = Flask(__name__)

    @app.route('/microservicio/busqueda_proveedor', methods=['GET'])
    def microserviceLogic ():

        try:
            if request.method =="GET":    
                if request.get_json()!= None:
                    req_data =request.get_json()
                    criteria = req_data['criteria']
                else:
                    criteria = request.args.get('criteria')
                    

                db = MySQLdb.connect(host="54.85.114.57", user="freddyjesus0", passwd="FreJe9008",  port=3308, db="microservice", charset='utf8',use_unicode=True)        
                cur = db.cursor()
                query = ("SELECT * FROM microservicereceiver_catalog WHERE provider like %s")
                criteria= "%"+criteria+"%"
                cur.execute(query, [criteria])
                rows = cur.fetchall()
                items =[]
                for row in rows:
                    items.append(json.dumps(row, indent=4, sort_keys=True, default=str))
                    print (json.dumps(row, indent=4, sort_keys=True, default=str))    
                db.close()
                response =json.dumps({'catalog':items}, indent=4, sort_keys=True, default=str)
                return response
                
        except ConnectionError as e:
            print ("Error en conexión a url ".url)

    if __name__ == '__main__':
        app.run(host="0.0.0.0", debug=True, port=5001)
        

#Microservice.microserviceLogic(sys.argv[1], sys.argv[2], sys.argv[3])
#Microservice.get_http(sys.argv[3])
#Microservice.queuePublishMessage()

   

