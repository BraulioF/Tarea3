""" views models"""
import models
from models.sale_order.venta import saleOrder
from models.sale_order_line import resources as rs_product
from models.product.resources import ResProductGet
from flask import Flask, jsonify, request
from models import *
from models import odoo

""" import librery"""
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
    partners = rs_partner.ResPartnerList.res_partner()
    return jsonify(partners)

#Views parnter list
@app.route("/partner/create", methods=["POST"])
#Enviar a la ruta a traves de postman un json con el name el phone y el email
def create():
    #capturo json
    data = request.get_json()
    cliente = data["cliente"]
    print(cliente)
    
    crear = rs_partner.ResPartnerCreate.post(cliente)
    #y lo mando a su resource
    return crear

@app.route("/partner/<id>", methods=["PUT"])
def update_partner(id):

    partners = rs_partner.ResPartnerGetByID.get_by_id(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        data = request.get_json()
        rs_partner.ResPartnerUpdate.update_by_id(id,data)
        return jsonify(partners)

@app.route("/partner/drop/<id>", methods=["DELETE"])
def drop_partner(id):    
    partners = rs_partner.ResPartnerGetByID.get_by_id(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        #data = request.get_json()
        verificar =rs_partner.ResPartnerDelete.delete_by_id(id)
        return jsonify(verificar)

#POST A VENTAS
# @app.route("/venta/<id>", methods=["POST"])
# def create_venta(id):
#     #Usar el metodo ya creado donde creamos un partner
#     partners = rs_partner.ResPartnerGetByID.get_by_id(id)
#     data = request.get_json()
#     if(len(partners)== 0):
#         cliente = data["cliente"]    
#         rs_partner.ResPartnerCreate.post(cliente)
#         idpatner = create()
#         print("se creo con ", idpatner)
#     else:
#         idpatner = id
    
#     product = ResProductGet.get_default_code(data)
#     if(len(product)== 0):
#         return"No existe ese Producto"       
#     else:
#         order = data["venta"] 
#         saleOrder.order_create(order,idpatner)
#         order_line = data["producto"]
#         #rs_product.sale_order_line.order_line_create(order_line)
    
    return jsonify({"creado":order_line})
@app.route("/venta/<id>", methods=["POST"])
def create_venta(id):
    #Usar el metodo ya creado donde creamos un partner
    #partners = rs_partner.ResPartnerGetByID.get_by_id(id)
    data = request.get_json()    
    #order_line = data['producto']
    #print(order_line)
    rs_product.sale_order_line.order_line_create(data)
    
    return jsonify({"creado":data})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

    {
  "cliente":{
            "name": "Don Bosco",
            "rut" : "2222-2",
            "comment" : "Sin comentarios",
            "phone" : "555666777888",
            "email" : "donbosco@gmail.com"
  },
  "venta":{           
            "team_id" : "1",
            "partner_invoice_id" : "12148",
            "partner_shipping_id" : "12148",
            "payment_acquirer_id" : "2",
            "pricelist_id" : "1",
            "order_line" : "16899"                       
  },
  "producto":{    
            "default_code" : "20325",
            "order_line" : "7047",
            "order_id" : "",
            "order_partner_id" : "1363",               
            "product_id" : "10307",
            "product_uom_qty": "12",
            "price_unit": "1500"
  }
         
}