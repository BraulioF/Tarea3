from ..auth import odoo 

class saleOrder():
    """Odoo model: res.partner list for customer and company"""

    ##CREAR ORDER
    def order_create(data,idpatner):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'create', 
            
            [{
            'partner_id': idpatner,
            'team_id' : data['team_id'],
            'partner_invoice_id' : data['partner_invoice_id'],
            'partner_shipping_id' : data['partner_shipping_id'],
            'payment_acquirer_id' : data['payment_acquirer_id'],
            'pricelist_id' : data['pricelist_id'],                              
            }])

        print("Quizas y solo Quizas esta sea la order_id", id)   
        name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'name_get', [[id]])
        return id

    