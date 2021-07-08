from ..auth import odoo 

class saleOrder():
    """Odoo model: res.partner list for customer and company"""

    ##CREAR ORDER
    def order_create(data):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'create', 
            [{
            'partner_id': data["partner_id"],
            'team_id' : data['team_id'],
            'partner_invoice_id' : data['partner_invoice_id'],
            'partner_shipping_id' : data['partner_shipping_id'],
            'pricelist_id' : data['pricelist_id'],
            'product_id' : data['product_id'],
            #'name' : data['name'],
            'product_uom_qty': data['product_uom_qty'],
            'product_uom': data['product_uom'],
            'price_unit': data['price_unit'],           
            }])
        name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'name_get', [[id]])
        return name
    
    