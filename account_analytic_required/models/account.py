from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class AccountAccount(models.Model):
    _inherit = 'account.account'

    analytic_account_required = fields.Boolean(
        string='Cuenta analitica requerida?',
        help="Nos permite configurar si la cuenta analitica es requerida en la linea de factura en la cual se selecciona la actual cuenta.",
    )


    analytic_tag_required = fields.Boolean(
        string='Etiqueta analitica requerida?',
        help="Nos permite configurar si la etiqueta analitica es requerida en la linea de factura en la cual se selecciona la actual cuenta.",
    )