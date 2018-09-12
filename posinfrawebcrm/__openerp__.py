# -*- coding: utf-8 -*-
{
    'name': "POSinfraestructuraWEB.CRM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This module modifies POS WEB integration and CRM inventory magnament for infrastructure.
        Este modulo modifica la integracion POS WEB y CRM con gestion de inventario para infraestructura.
    """,

    'author': "SCL-SOFTWEB365",
    'website': "http://www.softweb365.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [        
        #'security/access.infrasan.xml',
        #'security/ir.model.access.csv'
        'views/views.xml', 
        'views/templates.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
