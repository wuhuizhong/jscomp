# -*- coding: utf-8 -*-
# 康虎软件工作室
# http://www.khcloud.net
# QQ: 360026606
# wechat: 360026606
#--------------------------
#

{
    'name': "cf_report_designer",

    'summary': """
        康虎云报表字段定义设计器
        """,

    'description': """
康虎云报表字段定义设计器
============================
本模块用以实现可视化定义报表所需的字段、使用的模板等信息。
定义后，在打印报表时即可自动生成报表数据，无需手工在QWeb模板中定义。


本模块主要功能：
----------------------------
* 定义报表所需字段
* 定义报表使用的模板
* 自动生成报表定义
* 自动生成报表数据文件

剩下的事情就是在康虎云报表设计器中设计报表模板并打印即可
    """,

    'author': "CFSoft Studio 【康虎软件工作室（QQ：360026606， 微信：360026606）】",
    'website': "http://www.khcloud.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'cfsoft',
    'version': '12.0.0.6',
    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['base', 'cfprint'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        "data/cfprint_templates.xml",
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}