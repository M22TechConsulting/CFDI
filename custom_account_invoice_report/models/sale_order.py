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

    @api.model
    def _amount_to_text_proforma(self):
        self.ensure_one()

        currency_name = self.currency_id.name.upper()

        currency_type = 'M.N' if currency_name == 'MXN' else 'M.E.'

        amount_i, amount_d = divmod(self.amount_total, 1)
        amount_d = round(amount_d, 2)
        amount_d = int(round(amount_d * 100, 2))

        words = self.currency_id.with_context(lang=self.partner_id.lang or 'es_ES').amount_to_text(amount_i).upper()
        return '%(words)s %(amount_d)02d/100 %(currency_type)s' % {
            'words': words,
            'amount_d': amount_d,
            'currency_type': currency_type,
        }



