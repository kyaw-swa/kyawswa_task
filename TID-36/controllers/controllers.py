# -*- coding: utf-8 -*-
# from odoo import http


# class TripRoute(http.Controller):
#     @http.route('/trip_route/trip_route', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trip_route/trip_route/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trip_route.listing', {
#             'root': '/trip_route/trip_route',
#             'objects': http.request.env['trip_route.trip_route'].search([]),
#         })

#     @http.route('/trip_route/trip_route/objects/<model("trip_route.trip_route"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trip_route.object', {
#             'object': obj
#         })
