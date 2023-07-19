{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle
    Registration and Ownership of each motorcycled of the brand.""",
    'author': 'ivgm-odoo',
    'website': 'https://github.com/ivgm-odoo/custom-addons',
    'category': 'Kawiil/Kawiil',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [
        'security/kawiil_groups.xml',
        'security/ir.model.access.csv',
        'security/kawiil_security.xml'
    ],
    'demo': [
        'demo/kawiil_demo.xml'
    ],
    'application': True,
}