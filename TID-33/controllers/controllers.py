# -*- coding: utf-8 -*-
# from odoo import http


# class HyperlinkLog(http.Controller):
#     @http.route('/hyperlink_log/hyperlink_log', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hyperlink_log/hyperlink_log/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hyperlink_log.listing', {
#             'root': '/hyperlink_log/hyperlink_log',
#             'objects': http.request.env['hyperlink_log.hyperlink_log'].search([]),
#         })

#     @http.route('/hyperlink_log/hyperlink_log/objects/<model("hyperlink_log.hyperlink_log"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hyperlink_log.object', {
#             'object': obj
#         })
