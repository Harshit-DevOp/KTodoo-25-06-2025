{
    'name': 'Salesforce Integration',
    'version': '1.0',
    'category': 'Integration',
    'license': 'LGPL-3',
    'summary': 'Integrate Odoo with Salesforce',
    'depends': ['base', 'contacts'],
    'demo': [
        'security/ir.model.access.csv',
        'views/salesforce_sync_views.xml',
    ],
    'installable': True,
    'application': True,
}

