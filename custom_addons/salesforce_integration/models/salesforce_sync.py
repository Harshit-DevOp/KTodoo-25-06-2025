import requests
from odoo import api, fields, models

class SalesforceSync(models.Model):
    _name = 'salesforce.sync'
    _description = 'Sync Salesforce with Odoo'

    @api.model
    def sync_salesforce_accounts(self):
        access_token = '00DQy00000Bt3bj!AQEAQFyj.DKnQdeXfaqZGWOyAsxOfflOuvt8RkLkCtW6iGA5_wwDiSwNlE7KT8IDi0Oe04k71H1x1OIowmYPbJ362knKooBK'
        instance_url = 'https://techcooperssoftwaresoluti20-dev-ed.develop.my.salesforce.com'

        url = f"{instance_url}/services/data/v57.0/sobjects/Account"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            accounts = response.json()
            for account in accounts.get('records', []):
                self.env['res.partner'].create_or_update_account(account)
        else:
            raise Exception(f"Salesforce API error: {response.text}")

    def create_or_update_account(self, account_data):
        account = self.env['res.partner'].search([('salesforce_id', '=', account_data['Id'])], limit=1)
        if not account:
            self.env['res.partner'].create({
                'name': account_data['Name'],
                'salesforce_id': account_data['Id']
            })
        else:
            account.write({
                'name': account_data['Name']
            })
