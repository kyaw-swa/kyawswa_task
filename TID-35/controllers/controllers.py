# -*- coding: utf-8 -*-
# from odoo import http


# class RemoveAction(http.Controller):
#     @http.route('/remove_action/remove_action', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/remove_action/remove_action/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('remove_action.listing', {
#             'root': '/remove_action/remove_action',
#             'objects': http.request.env['remove_action.remove_action'].search([]),
#         })

#     @http.route('/remove_action/remove_action/objects/<model("remove_action.remove_action"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('remove_action.object', {
#             'object': obj
#         })
