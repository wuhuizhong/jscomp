# from myaddons.reportbo_print.print_fun.print_execute_sql import print_execute_sql
#
#
# def print_data_table(self, bo, bill_id, id):
#     sql = """
#             select print_model_id,field_name_en,field_name_cn
#             from print_design_field
#             where print_model_id
#                 in (select id
#                     from print_design_bill2model
#                     where print_design_bill_id = '%s'
#                     and location = '2')
#             and field_name_cn = '%s'
#         """ % (bill_id, bo)
#     fields = print_execute_sql(self, sql)
#     if len(fields) != 0:
#         for foo in fields:
#             print(foo['print_model_id'])
#             print_model_id = foo['print_model_id']
#             print(foo['field_name_en'])
#             field_name_en = foo['field_name_en']
#             print(foo['field_name_cn'])
#             field_name_cn = foo['field_name_cn']
#         sql = """
#             select model_id
#             from print_design_bill2model
#             where id = '%s'
#         """ % print_model_id
#         model_id = print_execute_sql(self, sql)
#         # print(model_id)
#         for fo in model_id:
#             _model_id = fo['model_id']
#         sql = """
#             select model from ir_model where id = '%s'
#         """ % _model_id
#         _model_id = print_execute_sql(self, sql)
#         for f in _model_id:
#             _model_id_ = f['model'].replace('.', '_')
#         sql_modelId_table = """
#                         select id,relation
#                         from print_design_bill2model
#                         where print_design_bill_id = '%s'
#                         and location = '2' and model_id = '%s'
#                     """ % (bill_id, fo['model_id'])
#         modelId_table = print_execute_sql(self, sql_modelId_table)
#         for too in modelId_table:
#             print(too['relation'])
#         _sql_ = {
#             "field": field_name_en +" as "+ field_name_cn,
#             "from": _model_id_,
#             "where": too['relation']
#         }
#     else:
#         _sql_ = {}
#
#     return _sql_
