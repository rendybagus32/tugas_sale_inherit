from odoo import models


class Inherit_Sale(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        for record in self:
            bom = record.order_line.product_id.bom_ids.id
            if bom:
                self.env['mrp.production'].create(
                    {
                    'product_id': record.order_line.product_id.id,
                    'product_qty': record.order_line.product_uom_qty,
                    'product_uom_id': record.order_line.product_uom.id,
                    'bom_id': record.order_line.product_id.bom_ids.id,
                    })
            else:
                pass