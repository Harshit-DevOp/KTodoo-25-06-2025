from odoo import models, fields

class TallyXMLTag(models.Model):
    _name = 'tally.xml.tag'
    _description = 'Tally XML Tags'

    name = fields.Char(required=True)
    description = fields.Text()
