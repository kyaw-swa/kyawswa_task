from odoo import models, fields, api

class Trip(models.Model):
    _name = 'trip.route'
    _description = 'Trip Model'

    name = fields.Char(string='Trip Route')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    city = fields.Char(string='City')
    township = fields.Char(string='Township')
