# flake8: noqa
import json
from odoo.tools import float_is_zero
from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        move_lines = self.mapped('line_ids').filtered(
            lambda x: (
                x.account_id.analytic_account_required)
            and not x.analytic_account_id)
        if move_lines:
            raise UserError(_(
                "Algunas lineas no poseen cuenta analitica y "
                "las cuentas analiticas son requeridas para algunas de las cuentas seleccionadas.\n"
                "Cuentas: %s\n" % (
                    ", ".join(move_lines.mapped('account_id.name'))
                )
            ))

        move_lines = self.mapped('line_ids').filtered(
            lambda x: (
                          x.account_id.analytic_tag_required)
                      and not x.analytic_tag_ids)
        if move_lines:
            raise UserError(_(
                "Algunas lineas no poseen etiqueta analitica y "
                "las etiquetas analiticas son requeridas para algunas de las cuentas seleccionadas.\n"
                "Cuentas: %s\n" % (
                    ", ".join(move_lines.mapped('account_id.name'))
                )
            ))


        res = super(AccountMove, self).action_post()



        return res


