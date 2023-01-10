from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_product_lot_ids(self, product_id):
        lot_names = []
        for picking in self.picking_ids.filtered(lambda pick: pick.state != 'cancel'):
            lot_ids = picking.move_line_ids_without_package.filtered(lambda line: line.product_id.id == product_id.id).mapped("lot_id").mapped("name")
            if lot_ids:
                lot_names += lot_ids
        return lot_names



