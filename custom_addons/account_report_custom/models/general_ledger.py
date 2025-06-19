from odoo import models

class GeneralLedgerCustomHandlerInherit(models.AbstractModel):
    _inherit = 'account.general.ledger.report.handler'


    def _get_aml_values(self, report, options, expanded_account_ids, offset=0, limit=None):
        rslt = {account_id: {} for account_id in expanded_account_ids}
        aml_query = self._get_query_amls(report, options, expanded_account_ids, offset=offset, limit=limit)
        self._cr.execute(aml_query)
        aml_results_number = 0
        has_more = False
        for aml_result in self._cr.dictfetchall():
            if aml_result['partner_id']:
                partner_id = aml_result.get('partner_id')
                partner = self.env['res.partner'].browse(partner_id)
                if partner:
                    aml_result['gst'] = partner.vat
                else:
                    aml_result['gst'] = False

            aml_results_number += 1
            if aml_results_number == limit:
                has_more = True
                break

            if aml_result['ref'] and aml_result['account_type'] != 'asset_receivable':
                aml_result['communication'] = f"{aml_result['ref']} - {aml_result['name']}"
            else:
                aml_result['communication'] = aml_result['name']

            aml_key = (aml_result['id'], aml_result['date'])

            account_result = rslt[aml_result['account_id']]
            if not aml_key in account_result:
                account_result[aml_key] = {col_group_key: {} for col_group_key in options['column_groups']}

            already_present_result = account_result[aml_key][aml_result['column_group_key']]
            if already_present_result:
                already_present_result['debit'] += aml_result['debit']
                already_present_result['credit'] += aml_result['credit']
                already_present_result['balance'] += aml_result['balance']
                already_present_result['amount_currency'] += aml_result['amount_currency']
            else:
                account_result[aml_key][aml_result['column_group_key']] = aml_result
        return rslt, has_more




