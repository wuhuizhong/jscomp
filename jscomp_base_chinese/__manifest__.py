# -*- coding: utf-8 -*-


{
    'name': "jscomp初始化数据",
    'version': '1.0',
    'author': 'John Lin',
    'category': 'Base',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Chinese enhance. Out of the box use in china.
    Set all chinese default value.
    Default country, timezone, currency, partner... 
    """,
    'description': """
    
    odoo Chinese Enhance. 中国化增强-基础
    1. 中文默认值，如国家、时区、货币等。处理模块 base, product.
    2. 客户加简称，地址显示中文化，客户编码显示优先
    3. todo:中文演示数据(只有demo模式才加载)
    
    """,
    'pre_init_hook': 'pre_init_hook',
    'depends': [
        'base',
        'product',
        'l10n_cn'
    ],
    'data': [
        'views/res_partner_category_views.xml',
        'views/res_partner_views.xml',
        'data/ir_default_data.xml',
        'data/ir_sequence_data.xml',
        'data/base_data.xml',
        'data/res_currency_data.xml',
        'data/product_data.xml',
        'data/product_pricelist_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
