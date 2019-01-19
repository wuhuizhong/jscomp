# -*- coding: utf-8 -*-
# Copyright 2016 Cédric Pigeon, ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Purchase Product Multi Add",
    'summary': """
        Purchase Product Multi Add """,
    'author': 'John Lin',
    'website': "www.jscomp.cn",
    'category': 'Purchase Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
    ],
    'data': [
        'wizards/purchase_import_products_view.xml',
        'views/purchase_view.xml',
    ],
}
