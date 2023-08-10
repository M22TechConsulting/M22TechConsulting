
from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        vals = super().create(vals)
        if vals.type == 'invoice':
            vals['vat'] = ""
        return vals
