{
    'name': 'Tally Zip Import',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Import Excel demo into Accounting Module',
    'depends': ['base', 'account'],
    'license': 'LGPL-3',
    'demo': [
        'security/ir.model.access.csv',
        'views/upload_excel_view.xml',
    ],
    'installable': True,
    'application': False,
}
