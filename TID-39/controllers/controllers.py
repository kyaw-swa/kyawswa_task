# -*- coding: utf-8 -*-
# from odoo import http


# class SaleValidation(http.Controller):
#     @http.route('/sale_validation/sale_validation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_validation/sale_validation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_validation.listing', {
#             'root': '/sale_validation/sale_validation',
#             'objects': http.request.env['sale_validation.sale_validation'].search([]),
#         })

#     @http.route('/sale_validation/sale_validation/objects/<model("sale_validation.sale_validation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_validation.object', {
#             'object': obj
#         })
