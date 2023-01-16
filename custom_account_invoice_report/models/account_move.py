from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_sale_order_partner_name(self):
        for rec in self:
            if rec.partner_id.vat == "XAXX010101000":
                sale_order_id = rec.env["sale.order"].search([('invoice_ids','=',rec.id)],limit=1)
                return sale_order_id.partner_id.commercial_partner_id.name if sale_order_id else rec.partner_id.commercial_partner_id.name
            else:
                return False


