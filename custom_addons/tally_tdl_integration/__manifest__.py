{
    'name': 'Tally TDL Integration',
    'version': '18.1',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'summary': 'Receive Data from Tally, Map Fields, and Push to Accounting',
    'author': 'harshit.j@selectiva.io',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/tally_ledger_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
