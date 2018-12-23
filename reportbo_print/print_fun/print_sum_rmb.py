# from myaddons.reportbo_print.print_fun.print_execute_sql import print_execute_sql
# from myaddons.reportbo_print.print_fun.print_rmb import Num2MoneyFormat
# from odoo.http import request
#
#
# def print_sum_rmb(self, parameters, id):
#     for foo in parameters:
#         for fo in foo['children']:
#             if fo['type'] == 'sum':
#                 field_sum_rmb = fo['expression']
#                 field_sum_rmb = field_sum_rmb.split(".")[1].split("}")[0]
#                 print(field_sum_rmb)
#                 sql_rmb = """
#                             UPDATE print_design_define SET fields_rmb = '%s' WHERE ID = '%s'
#                         """ % (field_sum_rmb, id)
#                 request.env.cr.execute(sql_rmb)
#
# def print_sum_rmb_data(self, formatId, bill_id_id, id):
#     print(formatId)
#     sql_get_field = """
#         select fields_rmb from print_design_define where id = '%s'
#     """ % formatId
#     sql_get_field_ = print_execute_sql(self, sql_get_field)
#     name_en = ''
#     for foo in sql_get_field_:
#         if len(foo['fields_rmb']) != 0:
#             i = foo['fields_rmb']
#             sql = """
#                 select print_design_field.field_name_en,print_design_bill2model.model_id
#                 from print_design_field ,print_design_bill2model
#                 where print_design_field.print_design_bill_id = '%s'
#                 and print_design_field.field_name_cn = '%s'
#                 and print_design_field.print_model_id = print_design_bill2model.id
#             """ % (bill_id_id, i)
#             field_name_en = print_execute_sql(self, sql)
#             # for foo in field_name_en:
#             #     if len(foo['field_name_en']) != 0:
#             #         name_en = foo['field_name_en']
#             for foo in field_name_en:
#                 rmb_model_id = foo['model_id']
#                 rmb_name_en = foo['field_name_en']
#             sql_model_name = """
#                 select model from ir_model where id = '%s'
#             """ % rmb_model_id
#             sql_model_name = print_execute_sql(self, sql_model_name)
#             for foo_model in sql_model_name:
#                 model_name = foo_model['model']
#                 model_name = model_name.replace('.', '_')
#             sql_data = """
#                 select sum(%s) as 合计 from %s where account_move_line.move_id = '%s'
#             """ % (rmb_name_en, model_name, id)
#             sum_data = print_execute_sql(self, sql_data)
#             for su in sum_data:
#                 sum_ = su['合计']
#             ss = Num2MoneyFormat(self, sum_)
#             sb = {'人民币大写':ss}
#     return sb
#
