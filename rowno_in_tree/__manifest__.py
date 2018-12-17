# -*- encoding: utf-8 -*-
{
    'name': "行号显示",
    'version': '1.0.0',
    'summary': '树/列视图中显示行号',
    'category': 'Other',
    'description': """实现在树/列视图中显示行号""",
    'author': 'John',
    "depends" : ['web'],
    'data': [
             'views/listview_templates.xml',
             ],
    'license': 'AGPL-3',
    'qweb': [
            ],  
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
