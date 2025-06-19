from odoo import models, fields

class TallyConfiguration(models.Model):
    _name = 'tally.configuration'
    _description = 'Tally Configuration'

    name = fields.Char(required=True)
    default_journal_ledger = fields.Many2one('account.journal', string='Default Journal Ledger')
    default_product_ledger = fields.Many2one('account.account', string='Default Tally Product Ledger')
    default_tax_ledger = fields.Many2one('account.tax', string='Default Tally Tax Ledger')
    bill_allocation_enabled = fields.Boolean(string='Enable Bill Allocation')
