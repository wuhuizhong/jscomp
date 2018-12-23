# from myaddons.reportbo_print.print_fun.print_execute_sql import print_execute_sql
#
#
# def print_get_id(self, bill_id_id):
#     sql = """
#         select min(id) from print_design_define where bills = '%s'
#     """ % bill_id_id
#     format_id = print_execute_sql(self, sql)
#     for foo in format_id:
#         format_id = foo['min']
#     return format_id