from odoo import models, fields, api

class TallyLedgerStaging(models.Model):
    _name = 'tally.ledger.staging'
    _description = 'Tally Ledger Staging Table'

    guid = fields.Char("External ID", required=True, readonly=True)  # 🔹 Make it read-only
    name = fields.Char("Ledger Name", required=True)
    parent = fields.Char("Parent Group")
    address = fields.Text("Address")
    state = fields.Char("State")
    country = fields.Char("Country")
    gstin = fields.Char("GSTIN")

    # 🔹 Allow mapping to ALL accounts, regardless of company
    odoo_account_id = fields.Many2one(
        'account.account',
        string="Mapped Odoo Account",
        domain="[]",  # 🔹 Remove company-based filtering
        required=False
    )

    pushed_to_accounting = fields.Boolean("Pushed to Accounting", default=False)

    def action_push_to_accounting(self):
        """Push selected records into the official Odoo Chart of Accounts."""
        for record in self:
            if not record.odoo_account_id:
                # 🔹 Find an existing account or create a new one
                account = self.env['account.account'].search([
                    ('name', '=', record.name),
                    ('company_id', '=', self.env.company.id)  # Ensure it's for the correct company
                ], limit=1)

                if not account:
                    account = self.env['account.account'].create({
                        'name': record.name,
                        'code': record.gstin or "N/A",
                        'user_type_id': self.env.ref('account.data_account_type_revenue').id
                    })

                # 🔹 Assign the account to the ledger record
                record.odoo_account_id = account.id

            record.pushed_to_accounting = True  # Mark as pushed
