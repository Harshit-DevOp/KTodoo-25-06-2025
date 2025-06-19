import base64
import pandas as pd
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountExcelImport(models.TransientModel):
    _name = 'account.excel.import'
    _description = 'Import Accounting demo from Excel'

    file = fields.Binary('Upload Excel File', required=True)
    file_name = fields.Char('File Name')

    def action_import_excel(self):
        if not self.file_name.endswith(('.xls', '.xlsx')):
            raise ValidationError('Please upload a valid Excel file.')

        # Decode file
        file_content = base64.b64decode(self.file)
        df = pd.read_excel(file_content, engine='openpyxl')

        # Expected columns from the sample Excel format
        required_columns = ['Date', 'Description', 'Amount', 'Account']
        if not all(col in df.columns for col in required_columns):
            raise ValidationError('Invalid Excel format! Please check the template.')

        # Process the demo
        account_model = self.env['account.move']
        for _, row in df.iterrows():
            account_model.create({
                'date': row['Date'],
                'ref': row['Description'],
                'line_ids': [(0, 0, {
                    'name': row['Description'],
                    'debit': row['Amount'] if row['Amount'] > 0 else 0.0,
                    'credit': -row['Amount'] if row['Amount'] < 0 else 0.0,
                    'account_id': self.env['account.account'].search([('code', '=', row['Account'])], limit=1).id,
                })],
            })

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Excel file imported successfully!',
                'type': 'rainbow_man',
            }
        }
