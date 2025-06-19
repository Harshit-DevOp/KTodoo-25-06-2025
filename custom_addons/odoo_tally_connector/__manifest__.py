{
    'name': 'Odoo Tally Connector v2',
    'version': '18.0',
    'summary': 'Integrate Odoo with Tally for seamless accounting.',
    'author': 'harshit.j@selectiva.io',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'depends': ['account', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tally_configuration_views.xml',
        'views/tally_xml_tags_views.xml',
        'views/tally_field_mapping_views.xml',
    ],
    'installable': True,
    'application': True,
}
