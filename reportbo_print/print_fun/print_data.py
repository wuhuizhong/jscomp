# from myaddons.reportbo_print.print_fun.print_data_table import print_data_table
# from myaddons.reportbo_print.print_fun.print_data_text import print_data_text
# from myaddons.reportbo_print.print_fun.print_execute_sql import print_execute_sql
# from myaddons.reportbo_print.print_fun.print_get_id import print_get_id
# from myaddons.reportbo_print.print_fun.print_sum_rmb import print_sum_rmb_data
#
#
# def print_data(self, modelName, id, formatId):
#     sql_model_id = """
#         SELECT ID FROM IR_MODEL WHERE MODEL = '%s'
#     """ % modelName
#     modelId = print_execute_sql(self, sql_model_id)
#     for foo in modelId:
#         modelId_id = foo['id']
#     sql_bill_id = """
#         SELECT ID FROM print_design_bill WHERE table_name = '%s'
#     """ % modelId_id
#     bill_id = print_execute_sql(self, sql_bill_id)
#     for foo in bill_id:
#         bill_id_id = foo['id']
#     format_id = print_get_id(self, bill_id_id)
#     sql_print_format = """
#         SELECT REPORT FROM PRINT_DESIGN_DEFINE WHERE BILLS = '%s' and id = '%s'
#     """ % (bill_id_id, formatId)
#     print_format = print_execute_sql(self, sql_print_format)
#     for f1 in print_format:
#         format = f1
#     sql_print_head = """
#         SELECT FIELDS_TEXT FROM PRINT_DESIGN_DEFINE WHERE BILLS = '%s' and id = '%s'
#     """ % (bill_id_id, formatId)
#     print_head = print_execute_sql(self, sql_print_head)
#     for foo in print_head:
#         dict = {}
#         print(foo['fields_text'])
#         if len(foo['fields_text']) > 2:
#             fields_text = foo['fields_text'][1:-1].replace('\"', '')
#             fields_text = fields_text.replace(' ', '')
#             fields_text = fields_text.split(",")
#             for fo in fields_text:
#                 data_text = print_data_text(self, fo, bill_id_id, id)
#                 for f in data_text:
#                     dict.update(f)
#     sql_get_field = """
#             select fields_rmb from print_design_define where id = '%s'
#         """ % formatId
#     sql_get_field_ = print_execute_sql(self, sql_get_field)
#     for fi in sql_get_field_:
#         print(fi['fields_rmb'])
#         if fi['fields_rmb'] is not None:
#             name_en = print_sum_rmb_data(self, formatId, bill_id_id, id)
#             dict.update(name_en)
#     dic = {'表头': dict}
#     sql_print_body = """
#         SELECT FIELDS_TABLE FROM PRINT_DESIGN_DEFINE WHERE BILLS = '%s' and id = '%s'
#     """ % (bill_id_id, formatId)
#     print_body = print_execute_sql(self, sql_print_body)
#     for boo in print_body:
#         fields_table = boo['fields_table'][1:-1].replace('\"', '')
#         fields_table = fields_table.replace(' ', '')
#         fields_table = fields_table.split(",")
#         print(fields_table)
#         fie = ''
#         fro = ''
#         whe = ''
#         for bo in fields_table:
#             if len(bo) != 0:
#                 data_table = print_data_table(self, bo, bill_id_id, id)
#                 fie += data_table['from']+'.'+data_table['field'] + ', '
#                 fro += data_table['from'] + ', '
#                 whe += data_table['where'] + ' and '
#         fie = fie[:-2]
#         fro = fro + modelName.replace('.', '_')
#         whe = whe + modelName.replace('.', '_')+'.id= %s' % id
#         # 去重复
#         fro = fro.replace(' ', '')
#         fro = fro.split(",")
#         fro = list(set(fro))
#         fro = str(fro).replace('\'', '')
#         fro = fro.replace('[', '')
#         fro = fro.replace(']', '')
#         # whe = whe.replace(' ', '')
#         whe = whe.split(",")
#         whe = list(set(whe))
#         whe = str(whe).replace('\'', '')
#         whe = whe.replace('[', '')
#         whe = whe.replace(']', '')
#
#         sql = """
#             select %s from %s where %s
#         """ % (fie, fro, whe)
#         data_table = print_execute_sql(self, sql)
#         dic_table = {'表体': data_table}
#     dic.update(dic_table)
#     return {
#         "report": format['report'],
#         "data": dic
#     }