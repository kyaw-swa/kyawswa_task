from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
            ('draft', "Quotation"),
            ('sent', "Quotation Sent"),
            ('sale', "Sales Order"),
            ('done', "Locked"),
            ('cancel', "Cancelled"),
        ])

    def action_confirm(self):
        for order in self:
            confirm = True  # Assume all lines have sufficient quantity
            for line in order.order_line:
                # Get the on-hand quantity for the product in the warehouse
                on_hand_quantity = self.get_product_on_hand_quantity(line.product_id, line.warehouse_id)

                # Check if the selected product quantity is greater than the on-hand quantity
                if line.product_id.type != 'service' and line.product_uom_qty > on_hand_quantity:
                    confirm = False
                    break

            if confirm:
                order.action_validation()

            else:
                raise ValidationError("You can not create sale order because the product quantity is greater than on hand quality. You might need a validation if you want to create sale order.")
                
    def action_validation(self):
        self.write({'state': 'sale'})

    def get_product_on_hand_quantity(self, product, warehouse):
        quant = self.env['stock.quant'].search([
            ('product_id', '=', product.id),
            ('location_id', 'child_of', warehouse.lot_stock_id.id),
        ], order='quantity', limit=1)
        return quant.quantity if quant else 0.0