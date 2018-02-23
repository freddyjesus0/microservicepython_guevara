#!/usr/bin/python
import MySQLdb
import json
import sys
from flask import Flask, request 


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
                

            db = MySQLdb.connect(host="54.211.149.240", user="freddyjesus0", passwd="FreJe9008",  port=3308, db="microservice", charset='utf8',use_unicode=True)        
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
            
    except IOError as e:
        print ("Error en conexion a url ".url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5004)


   

