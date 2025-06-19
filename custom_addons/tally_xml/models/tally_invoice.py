class TallyInvoice(models.Model):
    _name = 'tally.invoice'
    _description = 'Tally Invoice Mapping'

    name = fields.Char(string="Invoice Reference", required=True)
    partner_id = fields.Many2one('res.partner', string="Customer")
    date_invoice = fields.Date(string="Invoice Date")
    amount_total = fields.Float(string="Total Amount")
    tally_sync_status = fields.Selection([
        ('pending', 'Pending'),
        ('exported', 'Exported'),
        ('failed', 'Failed')
    ], default='pending')

    def action_generate_xml(self):
        """Generate XML for export"""
        self.tally_sync_status = 'exported'
