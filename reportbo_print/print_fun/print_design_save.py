# import re
#
# from odoo.http import request
#
#
# def print_design_save(self, param, id):
#     fields_head = []
#     fields_body = []
#     fields_rmb = []
#     for foo in param:
#         if foo['elementType'] == 'text':
#             field_head = foo['content']
#             g = re.search("\${.*\}", foo['content'])
#             if g:
#                 field_head = field_head.split(".")[1].split("}")[0]
#                 if field_head != '合计' and field_head != '人民币大写':
#                     fields_head.append(field_head)
#         elif foo['elementType'] == 'table':
#             for con in foo['contentDataRows']:
#                 for row in con['columnData']:
#                     field_body = row['content']
#                     print(field_body)
#                     field_body = field_body.split("{")[1].split("}")[0]
#                     fields_body.append(field_body)
#     sql_head = """
#         UPDATE print_design_define SET fields_text = '%s' WHERE ID = '%s'
#     """ % (str(fields_head).replace('\'', '\"'), id)
#     request.env.cr.execute(sql_head)
#     sql_body = """
#         UPDATE print_design_define SET fields_table = '%s' WHERE ID = '%s'
#     """ % (str(fields_body).replace('\'', '\"'), id)
#     request.env.cr.execute(sql_body)
#     return 1