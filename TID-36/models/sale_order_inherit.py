from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    route_id = fields.Many2one('trip.route', string='Trip Route')

    @api.onchange('route_id')
    def _onchange_route_id(self):
        if self.route_id:
            # Get the city from the selected trip
            trip_city = self.route_id.city

            # Filter the available customers based on the trip's city
            allowed_customers = self.env['res.partner'].search([('city', '=', trip_city)])

            # Update the domain of the customer field to restrict the available options
            return {'domain': {'partner_id': [('id', 'in', allowed_customers.ids)]}}
        else:
            # If no trip is selected, remove any domain restriction
            return {'domain': {'partner_id': []}}

    @api.constrains('partner_id', 'route_id')
    def _check_customer_city(self):
        for order in self:
            if order.route_id and order.partner_id:
                if order.partner_id.city != order.route_id.city:
                    raise ValidationError("The selected customer must be from the same city as the trip.")
