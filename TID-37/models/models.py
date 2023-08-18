# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class quotation_without_debug(models.Model):
#     _name = 'quotation_without_debug.quotation_without_debug'
#     _description = 'quotation_without_debug.quotation_without_debug'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
