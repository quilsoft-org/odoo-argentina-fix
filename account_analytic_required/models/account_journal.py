from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class AccountJournal(models.Model):

    _inherit = 'account.journal'

    def _get_tax_settlement_entry_vals(self, lines_vals):
        """
        Esta funcion recibe las values de las lineas de liquidación (lineas
        que van a liquidar lo que se haya solicitado liquidar) y genera
        los vals para generar el asiento.
        Por ahora sacamos la liquidación de la parte en otra moneda ya que
        ensucia más que ayudar
        """
        self.ensure_one()

        balance = sum(map(lambda x: x['debit'] - x['credit'], lines_vals))

        # si el balance es distinto de cero agregamos cuenta contable
        if not self.company_id.currency_id.is_zero(balance):
            # check account payable
            account = self.default_account_id
            if balance >= 0.0:
                debit = 0.0
                credit = balance
            else:
                debit = -balance
                credit = 0.0

            if not account:
                raise ValidationError(_(
                    'Esta intentando crear un asiento automático desbalanceado'
                    '. Es posible que haya un error en el informe o '
                    'esté faltando configurar la cuenta de contrapartida en el'
                    'diario.'))
            lines_vals.append({
                'partner_id': self.settlement_partner_id.id,
                'name': self.name,
                'debit': debit,
                'credit': credit,
                'account_id': account.id,
            })

        # convertimos los vals a formato para crear en o2m
        line_ids = []
        for vals in lines_vals:
            line_ids.append((0, False, vals))

        move_vals = {
            'ref': self._context.get('entry_ref', self.name),
            'date': self._context.get('entry_date', fields.Date.today()),
            'journal_id': self.id,
            'company_id': self.company_id.id,
            'line_ids': line_ids,
        }
        return move_vals