# -*- coding: utf-8 -*-
{
    'name': 'Les Marques des les produits en vente',
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'summary': 'Les Marques des les produits en vente',
    'description': 'Les Marques des les produits en vente, odoo15',
    'author':'WAMANU',
    'maintainer': 'WAMANU',
    'website': 'http://www.wamanu.com',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/brand_views.xml',
        'views/sale_report_views.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
