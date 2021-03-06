from ..auth import odoo 
class ProductCategory ():
    def getCategory(data):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        product = data["create_prod"]
        parners_details = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                        'product.category', 'search_read',
                [[['name', '=', product["categ_name"]]]],
                { 'fields': ['id'] ,'limit': 1})
        return parners_details    