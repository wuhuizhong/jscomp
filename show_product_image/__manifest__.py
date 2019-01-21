# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': '显示产品图片',
    'author':"John Lin" ,
    'category': 'Sales Management',
    'summary': '产品销售订单显示图片',
    'license': 'AGPL-3',
    'website': 'http://www.jscomp.cn',
    'version': '1.1.0',
    'sequence': 1,
    'depends': ['sale', 'web_tree_image','purchase'],
    'data': [
        'views/show_product_view.xml',
    ],
    'installable': True,
}
