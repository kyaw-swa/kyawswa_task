# -*- coding: utf-8 -*-
# from odoo import http


# class HidingFields(http.Controller):
#     @http.route('/hiding_fields/hiding_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hiding_fields/hiding_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hiding_fields.listing', {
#             'root': '/hiding_fields/hiding_fields',
#             'objects': http.request.env['hiding_fields.hiding_fields'].search([]),
#         })

#     @http.route('/hiding_fields/hiding_fields/objects/<model("hiding_fields.hiding_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hiding_fields.object', {
#             'object': obj
#         })
