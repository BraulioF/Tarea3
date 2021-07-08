""" views models"""
from models.sale_order.venta import saleOrder
from flask import Flask, jsonify, request
from models import *
from models import odoo

""" import librery"""
import datetime
import time
import config as cg

#Global varial
HOST = cg.server['host']

#Declare app
app = Flask(__name__)


#Views parnter list
@app.route("/partner", methods=["GET"])
def search_read():
#    parnters = rs_partner.ResPartnerList.res_partner()
#    return jsonify(parnters)
    partners = rs_partner.ResPartnerList.ObtenerPartnerSegunID()
    return jsonify(partners)

#Views parnter list
@app.route("/partner/create", methods=["POST"])
#Enviar a la ruta a traves de postman un json con el name el phone y el email
def create():
    #capturo json
    name = request.json['name']
    rut = request.json['rut']
    comment = request.json['comment']
    phone = request.json['phone']
    email = request.json['email']
    crear = rs_partner.ResPartnerList.partner_create(name,rut,comment,phone,email)
    #y lo mando a su resource
    return jsonify({'Creado':crear})

@app.route("/partner/<id>", methods=["PUT"])
def update_partner(id):

    partners = rs_partner.ResPartnerList.ObtenerPartnerSegunID(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        data = request.get_json()
        rs_partner.ResPartnerList.ActualizarPartnerSegunID(id,data)
        return jsonify(partners)

@app.route("/partner/drop/<id>", methods=["DELETE"])
def drop_partner(id):    
    partners = rs_partner.ResPartnerList.ObtenerPartnerSegunID(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        #data = request.get_json()
        verificar =rs_partner.ResPartnerList.EliminarSegunID(id)
        return jsonify(verificar)

#POST A VENTAS
@app.route("/venta/<id>", methods=["POST"])
def create_venta(id):
    #Usar el metodo ya creado donde creamos un partner
    partners = rs_partner.ResPartnerList.ObtenerPartnerSegunID(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        data = request.get_json()
        saleOrder.order_create(data)
        # rs_partner.ResPartnerList.ActualizarPartnerSegunID(id,data)
        return jsonify({"creado?":data})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)