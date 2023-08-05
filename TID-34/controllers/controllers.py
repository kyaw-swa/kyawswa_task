# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderTemplateA5(http.Controller):
#     @http.route('/sale_order_template_a5/sale_order_template_a5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_template_a5/sale_order_template_a5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_template_a5.listing', {
#             'root': '/sale_order_template_a5/sale_order_template_a5',
#             'objects': http.request.env['sale_order_template_a5.sale_order_template_a5'].search([]),
#         })

#     @http.route('/sale_order_template_a5/sale_order_template_a5/objects/<model("sale_order_template_a5.sale_order_template_a5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_template_a5.object', {
#             'object': obj
#         })
