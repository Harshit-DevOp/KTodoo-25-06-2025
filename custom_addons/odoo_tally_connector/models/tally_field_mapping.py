from odoo import models, fields

class TallyFieldMapping(models.Model):
    _name = 'tally.field.mapping'
    _description = 'Tally Field Mapping'

    odoo_field = fields.Char(required=True)
    tally_field = fields.Char(required=True)
    is_active = fields.Boolean(default=True)
