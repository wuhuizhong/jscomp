# -*- coding: utf-8 -*-
{
    'name': "采购订单默认供应商合同条款",

    'summary': """
        在供应商信息中内部备注作为采购订单默认合同条款""",

    'description': """
        在供应商信息中内部备注作为采购订单默认合同条款
    """,

    'author': "John Lin",
    'website': "http://www.jscomp.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}