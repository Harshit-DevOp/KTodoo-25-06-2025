from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class TallyAPI(http.Controller):

    @http.route('/api/tally/ledger', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_tally_data(self, **post):
        try:
            # ✅ Get JSON data
            data = request.get_json_data()
            _logger.info("📥 Received Data from Tally: %s", json.dumps(data, indent=4))

            if not data or 'DATA' not in data or 'LEDGER' not in data['DATA']:
                _logger.error("❌ Invalid or missing LEDGER data!")
                return {"status": "error", "message": "Invalid or missing LEDGER data"}

            ledgers = data['DATA']['LEDGER']  # Extract the LEDGER list
            updated_records = []
            created_records = []

            for ledger in ledgers:
                guid = ledger.get('GUID', '').strip()  # Ensure GUID is clean
                name = ledger.get('NAME', '').strip()
                parent = ledger.get('PARENT', '').strip()
                address = ledger.get('ADDRESS', '').strip()
                state = ledger.get('STATE', '').strip()
                country = ledger.get('COUNTRY', '').strip()
                gstin = ledger.get('GSTIN', '').strip()

                _logger.info(f"🔍 Processing Ledger: GUID={guid}, Name={name}, Parent={parent}, State={state}, Country={country}")

                # ✅ Check if the record exists by GUID
                existing_record = request.env['tally.ledger.staging'].sudo().search([('guid', '=', guid)], limit=1)

                if existing_record:
                    # ✅ Update existing record (Only update non-empty values)
                    updates = {}
                    if state:
                        updates['state'] = state
                    if country:
                        updates['country'] = country
                    if updates:
                        existing_record.sudo().write(updates)
                        updated_records.append(existing_record.id)
                        _logger.info(f"🔄 Updated Ledger: {existing_record.id} with State={state}, Country={country}")
                else:
                    # ✅ Create a new record if GUID is not found
                    new_record = request.env['tally.ledger.staging'].sudo().create({
                        'guid': guid,
                        'name': name,
                        'parent': parent,
                        'address': address,
                        'state': state,
                        'country': country,
                        'gstin': gstin
                    })
                    created_records.append(new_record.id)
                    _logger.info(f"✅ Created New Ledger: {new_record.id}")

            return {
                "status": "success",
                "message": "Processed ledgers successfully",
                "updated_records": updated_records,
                "created_records": created_records
            }

        except Exception as e:
            _logger.error("❌ API Error: %s", str(e))
            return {"status": "error", "message": str(e)}
