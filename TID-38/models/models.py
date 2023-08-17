# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class account_filter_wizard(models.Model):
#     _name = 'account_filter_wizard.account_filter_wizard'
#     _description = 'account_filter_wizard.account_filter_wizard'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
