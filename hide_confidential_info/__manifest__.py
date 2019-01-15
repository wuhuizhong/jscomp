# -*- coding: utf-8 -*-
{
    'name': "hide_confidential_info",

    'summary': """
        启用隐藏敏感信息""",

    'description': """
        隐藏敏感项目:
            - 产品成本价
            - 合作伙伴明细
            - 销售、采购订单中价格信息
    """,

    'author': "John Lin",
    'website': "www.jscomp.cn",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': ['base','sale','account','purchase'],

    'data': [
        'security/view_cost_price.xml',
        'security/view_partner_detail.xml',
        'security/view_price.xml',
        'views/hide_product_cost.xml',
        'views/hide_partner_detail.xml',
        'views/hide_price.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}