
from odoo import models


class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'

    def _l10n_mx_edi_get_40_values(self, move):
        vals = super()._l10n_mx_edi_get_40_values(move)
        vals["customer_name"] = self._l10n_mx_edi_clean_to_legal_name(move.partner_id.name)
        return vals
