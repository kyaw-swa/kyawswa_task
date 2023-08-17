# -*- coding: utf-8 -*-
# from odoo import http


# class AccountFilterWizard(http.Controller):
#     @http.route('/account_filter_wizard/account_filter_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_filter_wizard/account_filter_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_filter_wizard.listing', {
#             'root': '/account_filter_wizard/account_filter_wizard',
#             'objects': http.request.env['account_filter_wizard.account_filter_wizard'].search([]),
#         })

#     @http.route('/account_filter_wizard/account_filter_wizard/objects/<model("account_filter_wizard.account_filter_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_filter_wizard.object', {
#             'object': obj
#         })
