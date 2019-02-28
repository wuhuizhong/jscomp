# -*- coding: utf-8 -*-


{
    'name': 'Odoo stock location Tree',
    'version': '1.0',
    'category': 'OdTree',
    'sequence': 14,
    'license':'LGPL-3',
    'description': """
    display product in a product category tree
    """,
    'author': 'John Lin',
    'website': 'http://www.jscomp.cn',
    'images': [],
    'depends': ['odtree','stock'],
    'qweb': [

    ],
    'data': [
        'views/stock_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
