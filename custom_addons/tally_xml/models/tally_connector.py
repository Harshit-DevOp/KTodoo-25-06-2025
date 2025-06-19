from odoo import models, fields, api

class TallyConnector(models.Model):
    _name = 'tally.connector'
    _description = 'Tally Connector Integration'

    name = fields.Char(string="Configuration Name", required=True)
    company_id = fields.Many2one('res.company', string="Company", required=True)
    tally_url = fields.Char(string="Tally Server URL")
    default_journal = fields.Many2one('account.journal', string="Default Journal")
    state = fields.Selection([('draft', 'Draft'), ('connected', 'Connected')], default='draft')

    def action_connect(self):
        """Simulate connection to Tally"""
        self.state = 'connected'
