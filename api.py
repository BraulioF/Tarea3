""" views models"""
import models
from models.sale_order.venta import saleOrder, sale_order_coinsidencias
from models.sale_order_line import resources as rs_product
from models.product.resources import ProductCreate, ResProductGet
from models.crm_team import resources  as rs_crm_team
from models.product_categoria import resources as rs_pro_cat
from models.uom import resources as rs_uom

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
@app.route("/partner/create/<id>", methods=["POST"])
#Enviar a la ruta a traves de postman un json con el name el phone y el email
def create(id):
    #capturo json
    data = request.get_json()
    cliente = data["cliente"]
    print(cliente,id)
    
    crear = rs_partner.ResPartnerCreate.post(cliente,id)
    #y lo mando a su resource
    return crear

@app.route("/partner/", methods=["PUT"])
def update_partner():
    data = request.get_json()
    cliente = data["cliente"] 
    rut = cliente["rut"]
    partners = rs_partner.ResPartnerGetByID.get_by_rut(rut)
    first = partners[0]
    print(first["id"])
    if(len(partners)== 0):
        return "Ese RUT no existe"
    else:
        #print(partners)
        
        #rs_partner.ResPartnerUpdate.update_by_id(id,data)
        return jsonify(partners)

@app.route("/partner/drop/<id>", methods=["DELETE"])
def drop_partner(id):    
    partners = rs_partner.ResPartnerGetByID.get_by_rut(id)
    if(len(partners)== 0):
        return "Ese ID no existe"
    else:
        #print(partners)
        #data = request.get_json()
        verificar =rs_partner.ResPartnerDelete.delete_by_id(id)
        return jsonify(verificar)

#POST A VENTAS
@app.route("/venta", methods=["POST"])
def create_venta():
    #Usar el metodo ya creado donde creamos un partner
    data = request.get_json()

    coinsidences = rs_crm_team.crm_team_get.get_team(data)
    if(len(coinsidences) == 0):
        valor = data['venta']
        valoresp = valor['name']
        return "'" + valoresp +"'" + " No existe en la Base de Datos"
    else:
        value = coinsidences[0]
        idteam = value['id']
        get_team_repeticion = sale_order_coinsidencias.get_coinsidencia(data,idteam)
        if(len(get_team_repeticion) != 0):
            val = get_team_repeticion[0]
            idventa = val['name']
            return "Esa venta ya existe " + idventa
        else:       
            cliente = data["cliente"] 
            rut = cliente["rut"]
            partners = rs_partner.ResPartnerGetByID.get_by_rut(rut)
            if(len(partners)== 0):           
                crear = rs_partner.ResPartnerCreate.post(cliente)
                idpatner = crear
                print("se creo con ", crear)
            else:
                first = partners[0]
                idpatner = first["id"]
            
            product = ResProductGet.get_default_code(data)
            if(len(product)== 0):
                return"No existe ese Producto"       
            else:
                order = data["venta"] 
                order_id = saleOrder.order_create(order,idpatner,idteam)
                order_line = data["producto"]
                rs_product.sale_order_line.order_line_create(order_line,order_id)
            
            return jsonify({"creado":order_line})

@app.route("/product/create", methods=["POST"])
#Enviar a la ruta a traves de postman un json con el name el phone y el email
def createproduct():
    #capturo json
    data = request.get_json()
    verif = rs_pro_cat.ProductCategory.getCategory(data)
    product = data["create_prod"]
    if(len(verif)==0):        
        val = product["categ_name"]
        return "No existe la categoria :"+ val
    check = rs_uom.UomGet.get_uom(data)
    if(len(check)==0):
        val = product["uom_name"]
        return "No existe la unidad de medida :"+ val
    check_po = rs_uom.UomPoGet.get_uom_po(data)
    if(len(check_po)==0):
        val = product["uom_po_name"]
        return "No existe la unidad de medida :"+ val
        
    verif = verif[0]
    check = check[0]
    check_po = check_po[0]
    id_name_categ = verif['id']
    id_display_uom = check['id']
    id_display_uom_po = check_po['id']
    print(id_name_categ)
    print(id_display_uom)
    print(id_display_uom_po)
    crear = ProductCreate.post(product,id_name_categ,id_display_uom,id_display_uom_po)
    #y lo mando a su resource
    return jsonify(crear)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

# {
#   "cliente":{
#             "name": "Varian Wrynn",
#             "rut" : "99999-9",
#             "comment" : "Sin comentarios",
#             "phone" : "555666777888",
#             "email" : "kigvarian@gmail.com"
#   },
#   "venta":{           
#             "team_id" : "1",
#             "partner_invoice_id" : "12148",
#             "partner_shipping_id" : "12148",
#             "payment_acquirer_id" : "2",
#             "pricelist_id" : "1"
                                  
#   },
#   "producto":{    
#             "default_code" : "01005005",             
#             "product_id" : "7162",
#             "product_uom_qty": "12",
#             "price_unit": "1500"
#   }
         
# }