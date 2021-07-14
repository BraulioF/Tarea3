from ..auth import odoo 
class ResProductGet():
    def get_default_code (data):
            odoo_client = odoo.OdooClient()
            uid, models = odoo_client.logging()
            product = data["producto"]
            parners_details = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                            'product.template', 'search_read',
                [[['default_code', '=', product["default_code"]]]],
                { 'fields': ['default_code'] ,'limit': 1})
            return parners_details 
class ProductCreate():
    def post(data,id_name_categ,id_display_uom):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        productid = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'product.product', 'create', 
            [{ 
            "default_code": data["default_code"],
            "type":data["type"],
            "name":data["name"],
            "barcode":data["barcode"],
            "categ_id":id_name_categ,
            "ist_price":data["ist_price"],
            "standard_price":data["standard_price"],
            "uom_id":id_display_uom,
            "uom_po_id":data["uom_po_id"],
            "sale_ok":data["sale_ok"],
            "purchase_ok":data["purchase_ok"]
            }])
        #name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'res.partner', 'name_get', [[partnerid]])
        return productid

 