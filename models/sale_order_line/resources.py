from ..auth import odoo 

class sale_order_line():
    """Odoo model: res.partner list for customer and company"""

    def order_line_create(data):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        line_create = data["producto"]
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order.line', 'create', 
            [{
                #"default_code" : line_create["default_code"],           
                "product_id" : line_create["product_id"],
                "product_uom_qty": line_create["product_uom_qty"],
                "price_unit": line_create["price_unit"],  
                'order_id' : line_create["order_line"],      
            }])

            
        name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order.line', 'name_get', [[id]])
        return name
    ##Buscar el default_code en la tabla product.template

    
