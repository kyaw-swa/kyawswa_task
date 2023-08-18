from odoo import models, api

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.model
    def message_post(self, **kwargs):
        body = kwargs.get('body')
        if body:
            body += '<br/><a href="http://www.google.com" target="_blank">Google</a>'
            body += '<br/><a href="http://www.yahoo.com" target="_blank">Yahoo</a>'
            kwargs['body'] = body

        return super(SaleOrderInherit, self).message_post(**kwargs)
