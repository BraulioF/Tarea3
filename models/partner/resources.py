""" Module of res.partner odoo model """
from ..auth import odoo 



class ResPartnerList():
    """Odoo model: res.partner list for customer and company"""
    
    def res_partner():
        """ list partner get """
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        
        s_read = models.execute_kw(odoo_client.db, uid, odoo_client.password,
            'res.partner', 'search_read',
            [[['is_company', '=', True], ['customer', '=', True]]],
            {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        return s_read


    def partner_create(data):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'res.partner', 'create', 
            [{
            'name': data["name"],
            'rut' : data["rut"],
            'comment' : data["comment"],
            'phone' : data["phone"],
            'email' : data["email"]
            }])
        name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'res.partner', 'name_get', [[id]])
        return id
    
    def ObtenerPartnerSegunID(id):

        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()

        result = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                    'res.partner', 'search_read',
                    [[['id','=',id]]],
            {'fields': ['rut', 'comment', 'phone','email']})
                       
        return result
    
    def ActualizarPartnerSegunID(id, data):

        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        #12148 frank
        #12165  don cangrejo
        #12170

        models.execute_kw(odoo_client.db, uid, odoo_client.password, 'res.partner', 'write', [[int(id)], 
        {
             'name': data['name'],
             'rut' : data['rut'],
             'comment' : data['comment'],
             'phone' : data['phone'],
             'email': data['email']
        }])
    def EliminarSegunID(id):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        models.execute_kw(odoo_client.db, uid, odoo_client.password, 'res.partner', 'unlink', [[int(id)]])
        # check if the deleted record is still in the database
        check = models.execute_kw(odoo_client.db, uid, odoo_client.password,
            'res.partner', 'search', [[['id', '=', id]]])
        return check