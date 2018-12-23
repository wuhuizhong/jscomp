# from myaddons.reportbo_print.print_fun.print_execute_sql import print_execute_sql
#
#
# def print_data_text(self, field, bill_id, id):
#     sql_modelId_text = """
#         select id
#         from print_design_bill2model
#         where print_design_bill_id = '%s'
#         and location = '1'
#     """ % bill_id
#     modelId_text = print_execute_sql(self, sql_modelId_text)
#     # print(modelId_text)
#     sql = """
#         select print_model_id,field_name_en,field_name_cn
#         from print_design_field
#         where print_model_id
#             in (select id
#                 from print_design_bill2model
#                 where print_design_bill_id = '%s'
#                 and location = '1')
#         and field_name_cn = '%s'
#     """ % (bill_id, field)
#     fields = print_execute_sql(self, sql)
#     for foo in fields:
#         print(foo['print_model_id'])
#         print(foo['field_name_en'])
#         print(foo['field_name_cn'])
#     sql = """
#         select model_id
#         from print_design_bill2model
#         where id = '%s'
#     """ % foo['print_model_id']
#     model_id = print_execute_sql(self, sql)
#     # print(model_id)
#     for fo in model_id:
#         _model_id = fo['model_id']
#     sql = """
#         select model from ir_model where id = '%s'
#     """ % _model_id
#     _model_id = print_execute_sql(self, sql)
#     for f in _model_id:
#         _model_id_ = f['model'].replace('.', '_')
#     sql = """
#         select %s as %s from %s where id = '%s'
#     """ % (foo['field_name_en'], foo['field_name_cn'], _model_id_, id)
#     data = print_execute_sql(self, sql)
#     return data
#
#
#
