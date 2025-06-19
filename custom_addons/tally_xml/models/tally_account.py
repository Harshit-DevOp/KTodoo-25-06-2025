class TallyAccountLedger(models.Model):
    _name = 'tally.account.ledger'
    _description = 'Tally Account Ledger'

    name = fields.Char(string="Ledger Name", required=True)
    ledger_code = fields.Char(string="Ledger Code")
    balance = fields.Float(string="Balance")
