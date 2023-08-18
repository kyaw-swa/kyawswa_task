# -*- coding: utf-8 -*-
# from odoo import http


# class QuotationWithoutDebug(http.Controller):
#     @http.route('/quotation_without_debug/quotation_without_debug', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quotation_without_debug/quotation_without_debug/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quotation_without_debug.listing', {
#             'root': '/quotation_without_debug/quotation_without_debug',
#             'objects': http.request.env['quotation_without_debug.quotation_without_debug'].search([]),
#         })

#     @http.route('/quotation_without_debug/quotation_without_debug/objects/<model("quotation_without_debug.quotation_without_debug"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quotation_without_debug.object', {
#             'object': obj
#         })
