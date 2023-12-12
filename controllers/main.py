# private_website_sale/controllers/main.py
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class PrivateWebsiteSale(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        print("[PrivateWebsiteSale]shop")
        return super(PrivateWebsiteSale, self).shop(page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg, **post)


    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="user", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        print("[PrivateWebsiteSale]product")
        return super(PrivateWebsiteSale, self).product(product, category=category, search=search, **kwargs)

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="user", website=True, sitemap=False)
    def old_product(self, product, category='', search='', **kwargs):
        # Compatibility pre-v14
        print("[PrivateWebsiteSale]oldproduct")
        return super(PrivateWebsiteSale, self).old_product(product, category=category, search=search, **kwargs)

    @http.route(['/shop/change_pricelist/<model("product.pricelist"):pl_id>'], type='http', auth="user", website=True, sitemap=False)
    def pricelist_change(self, pl_id, **post):
        print("[PrivateWebsiteSale]pricelist_change")
        return super(PrivateWebsiteSale, self).pricelist_change(pl_id, **post)

    @http.route(['/shop/pricelist'], type='http', auth="user", website=True, sitemap=False)
    def pricelist(self, promo, **post):
        print("[PrivateWebsiteSale]pricelist")
        return super(PrivateWebsiteSale, self).pricelist(promo, **post)

    @http.route(['/shop/cart'], type='http', auth="user", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        print("[PrivateWebsiteSale]cart")
        return super(PrivateWebsiteSale, self).cart(access_token, revive, **post)

    @http.route(['/shop/cart/update'], type='http', auth="user", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        print("[PrivateWebsiteSale]cart update")
        return super(PrivateWebsiteSale, self).cart_update(product_id, add_qty, set_qty, **kw)

    @http.route(['/shop/cart/update_json'], type='json', auth="user", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, **kw):
        print("[PrivateWebsiteSale]cart update json")
        return super(PrivateWebsiteSale, self).cart_update_json(product_id, line_id, add_qty, set_qty, display, **kw)

    @http.route('/shop/save_shop_layout_mode', type='json', auth="user", website=True)
    def save_shop_layout_mode(self, layout_mode):
       return super(PrivateWebsiteSale, self).save_shop_layout_mode(layout_mode)

    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="user", website=True, sitemap=False)
    def address(self, **kw):
        return super(PrivateWebsiteSale, self).address(**kw)

    @http.route(['/shop/checkout'], type='http', auth="user", website=True, sitemap=False)
    def checkout(self, **post):
        print("[PrivateWebsiteSale]shop checkout")
        return super(PrivateWebsiteSale, self).checkout(**post)

    @http.route(['/shop/confirm_order'], type='http', auth="user", website=True, sitemap=False)
    def confirm_order(self, **post):
       return super(PrivateWebsiteSale, self).confirm_order(**post)

    # ------------------------------------------------------
    # Extra step
    # ------------------------------------------------------
    @http.route(['/shop/extra_info'], type='http', auth="user", website=True, sitemap=False)
    def extra_info(self, **post):
        return super(PrivateWebsiteSale, self).extra_info(**post)
    
    @http.route('/shop/payment', type='http', auth="user", website=True, sitemap=False)
    def shop_payment(self, **post):
        return super(PrivateWebsiteSale, self).shop_payment(**post)
    
    @http.route('/shop/payment/get_status/<int:sale_order_id>', type='json', auth="user", website=True)
    def shop_payment_get_status(self, sale_order_id, **post):
        return super(PrivateWebsiteSale, self).shop_payment_get_status(sale_order_id, **post)

    @http.route('/shop/payment/validate', type='http', auth="user", website=True, sitemap=False)
    def shop_payment_validate(self, transaction_id=None, sale_order_id=None, **post):
       return super(PrivateWebsiteSale, self).shop_payment_validate(transaction_id, sale_order_id, **post)

    @http.route(['/shop/confirmation'], type='http', auth="user", website=True, sitemap=False)
    def shop_payment_confirmation(self, **post):
        return super(PrivateWebsiteSale, self).shop_payment_confirmation(**post)

    @http.route(['/shop/print'], type='http', auth="user", website=True, sitemap=False)
    def print_saleorder(self, **kwargs):
        return super(PrivateWebsiteSale, self).print_saleorder(**kwargs)

    @http.route(['/shop/country_infos/<model("res.country"):country>'], type='json', auth="user", methods=['POST'], website=True)
    def country_infos(self, country, mode, **kw):
        return super(PrivateWebsiteSale, self).dict(country, mode, **kw)

    # --------------------------------------------------------------------------
    # Products Recently Viewed
    # --------------------------------------------------------------------------
    @http.route('/shop/products/recently_viewed_update', type='json', auth="user", website=True)
    def products_recently_viewed_update(self, product_id, **kwargs):
        return super(PrivateWebsiteSale, self).products_recently_viewed_update(product_id, **kwargs)

    @http.route('/shop/products/recently_viewed_delete', type='json', auth="user", website=True)
    def products_recently_viewed_delete(self, product_id, **kwargs):
        return super(PrivateWebsiteSale, self).products_recently_viewed_delete(product_id, **kwargs)