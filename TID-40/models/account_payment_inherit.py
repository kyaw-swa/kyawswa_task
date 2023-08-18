from odoo import models, fields, api

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    receipt_number = fields.Char(string='Receipt Number', readonly=True, copy=False)

    @api.model
    def create(self, vals):
        if not vals.get('receipt_number'):
            date_str = fields.Date.context_today(self)
            receipt_number = f'MM-{date_str}'
            existing_receipts = self.env['account.payment'].search_count([('receipt_number', 'like', receipt_number)])
            if existing_receipts:
                receipt_number += f'-{existing_receipts + 1}'
            vals['receipt_number'] = receipt_number
        return super(AccountPayment, self).create(vals)

    def print_receipt(self):
        # Check if receipt number is already generated
        if not self.receipt_number:
            date_str = fields.Date.context_today(self)
            receipt_number = f'MM-{date_str}'
            existing_receipts = self.env['account.payment'].search_count([('receipt_number', 'like', receipt_number)])
            if existing_receipts:
                receipt_number += f'-{existing_receipts + 1}'
            self.write({'receipt_number': receipt_number})

        # Call the super method to print the receipt PDF
        return super(AccountPayment, self).print_receipt()
