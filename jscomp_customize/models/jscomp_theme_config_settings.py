# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class jscompThemeConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'jscomp.theme.config.settings'

    _description = u"J&S Customize settings"
    jscomp_system_name = fields.Char('System Name', help=u"Setup System Name,which replace Odoo")
    jscomp_show_lang = fields.Boolean('Show Quick Language Switcher',
                                   help=u"When enable,User can quick switch language in user menu")
    jscomp_show_debug = fields.Boolean('Show Quick Debug', help=u"When enable,everyone login can see the debug menu")
    jscomp_show_documentation = fields.Boolean('Show Documentation', help=u"When enable,User can visit user manual")
    jscomp_show_documentation_dev = fields.Boolean('Show Developer Documentation',
                                                help=u"When enable,User can visit development documentation")
    jscomp_show_support = fields.Boolean('Show Support', help=u"When enable,User can vist your support site")
    jscomp_show_account = fields.Boolean('Show My Account', help=u"When enable,User can login to your website")
    jscomp_show_enterprise = fields.Boolean('Show Enterprise Tag', help=u"Uncheck to hide the Enterprise tag")
    jscomp_show_share = fields.Boolean('Show Share Dashboard', help=u"Uncheck to hide the Odoo Share Dashboard")
    jscomp_show_poweredby = fields.Boolean('Show Powered by Odoo', help=u"Uncheck to hide the Powered by text")
    jscomp_stop_subscribe = fields.Boolean('Stop Odoo Subscribe(Performance Improve)', help=u"Check to stop Odoo Subscribe function")
    group_show_author_in_apps = fields.Boolean(string="Show Author in Apps Dashboard", implied_group='jscomp_customize.group_show_author_in_apps',
                                               help=u"Uncheck to Hide Author and Website in Apps Dashboard")

    jscomp_documentation_url = fields.Char('Documentation Url')
    jscomp_documentation_dev_url = fields.Char('Developer Documentation Url')
    jscomp_support_url = fields.Char('Support Url')
    jscomp_account_title = fields.Char('My Odoo.com Account Title')
    jscomp_account_url = fields.Char('My Odoo.com Account Url')

    @api.model
    def get_values(self):
        ir_config = self.env['ir.config_parameter']
        jscomp_system_name = ir_config.sudo().get_param('jscomp_system_name', default='odooApp')

        jscomp_show_lang = True if ir_config.sudo().get_param('jscomp_show_lang') == "True" else False
        jscomp_show_debug = True if ir_config.sudo().get_param('jscomp_show_debug') == "True" else False
        jscomp_show_documentation = True if ir_config.sudo().get_param('jscomp_show_documentation') == "True" else False
        jscomp_show_documentation_dev = True if ir_config.sudo().get_param('jscomp_show_documentation_dev') == "True" else False
        jscomp_show_support = True if ir_config.sudo().get_param('jscomp_show_support') == "True" else False
        jscomp_show_account = True if ir_config.sudo().get_param('jscomp_show_account') == "True" else False
        jscomp_show_enterprise = True if ir_config.sudo().get_param('jscomp_show_enterprise') == "True" else False
        jscomp_show_share = True if ir_config.sudo().get_param('jscomp_show_share') == "True" else False
        jscomp_show_poweredby = True if ir_config.sudo().get_param('jscomp_show_poweredby') == "True" else False
        jscomp_stop_subscribe = True if ir_config.sudo().get_param('jscomp_stop_subscribe') == "True" else False

        jscomp_documentation_url = ir_config.sudo().get_param('jscomp_documentation_url',
                                                    default='http://www.odoo.com/documentation/user/12.0/en/index.html')
        jscomp_documentation_dev_url = ir_config.sudo().get_param('jscomp_documentation_dev_url',
                                                        default='http://www.odoo.com/documentation/12.0/index.html')
        jscomp_support_url = ir_config.sudo().get_param('jscomp_support_url', default='http://www.odoo.com/trial/')
        jscomp_account_title = ir_config.sudo().get_param('jscomp_account_title', default='My Online Account')
        jscomp_account_url = ir_config.sudo().get_param('jscomp_account_url', default='http://www.odoo.com/my-account/')
        return dict(
            jscomp_system_name=jscomp_system_name,
            jscomp_show_lang=jscomp_show_lang,
            jscomp_show_debug=jscomp_show_debug,
            jscomp_show_documentation=jscomp_show_documentation,
            jscomp_show_documentation_dev=jscomp_show_documentation_dev,
            jscomp_show_support=jscomp_show_support,
            jscomp_show_account=jscomp_show_account,
            jscomp_show_enterprise=jscomp_show_enterprise,
            jscomp_show_share=jscomp_show_share,
            jscomp_show_poweredby=jscomp_show_poweredby,
            jscomp_stop_subscribe=jscomp_stop_subscribe,

            jscomp_documentation_url=jscomp_documentation_url,
            jscomp_documentation_dev_url=jscomp_documentation_dev_url,
            jscomp_support_url=jscomp_support_url,
            jscomp_account_title=jscomp_account_title,
            jscomp_account_url=jscomp_account_url
        )

    @api.multi
    def set_values(self):
        self.ensure_one()
        ir_config = self.env['ir.config_parameter']
        ir_config.set_param("jscomp_system_name", self.jscomp_system_name or "")
        ir_config.set_param("jscomp_show_lang", self.jscomp_show_lang or "False")
        ir_config.set_param("jscomp_show_debug", self.jscomp_show_debug or "False")
        ir_config.set_param("jscomp_show_documentation", self.jscomp_show_documentation or "False")
        ir_config.set_param("jscomp_show_documentation_dev", self.jscomp_show_documentation_dev or "False")
        ir_config.set_param("jscomp_show_support", self.jscomp_show_support or "False")
        ir_config.set_param("jscomp_show_account", self.jscomp_show_account or "False")
        ir_config.set_param("jscomp_show_enterprise", self.jscomp_show_enterprise or "False")
        ir_config.set_param("jscomp_show_share", self.jscomp_show_share or "False")
        ir_config.set_param("jscomp_show_poweredby", self.jscomp_show_poweredby or "False")
        ir_config.set_param("jscomp_stop_subscribe", self.jscomp_stop_subscribe or "False")
        # ir_config.set_param("group_show_author_in_apps", self.group_show_author_in_apps or "False")

        ir_config.set_param("jscomp_documentation_url",
                            self.jscomp_documentation_url or "http://www.odoo.com/documentation/user/12.0/en/index.html")
        ir_config.set_param("jscomp_documentation_dev_url",
                            self.jscomp_documentation_dev_url or "http://www.odoo.com/documentation/12.0/index.html")
        ir_config.set_param("jscomp_support_url", self.jscomp_support_url or "http://www.odoo.com/trial/")
        ir_config.set_param("jscomp_account_title", self.jscomp_account_title or "My Online Account")
        ir_config.set_param("jscomp_account_url", self.jscomp_account_url or "http://www.odoo.com/my-account/")

        return True

    @api.multi
    def remove_sales(self):
        to_removes = [
            # 清除销售单据
            ['sale.order.line', ],
            ['sale.order', ],
            ['sale.order.template.option', ],
            ['sale.order.template.line', ],
            ['sale.order.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', '=', 'sale.order')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where code ='sale.order';"
            self._cr.execute(sql)
        except Exception as e:
            raise Warning(e)
        return True

    def remove_product(self):
        to_removes = [
            # 清除产品数据
            ['product.product', ],
            ['product.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号,针对自动产品编号
            seqs = self.env['ir.sequence'].search([('code', '=', 'product.product')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where code ='product.product';"
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_product_attribute(self):
        to_removes = [
            # 清除产品属性
            ['product.attribute.value', ],
            ['product.attribute', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_pos(self):
        to_removes = [
            # 清除POS单据
            ['pos.order.line', ],
            ['pos.order', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', '=', 'pos.order')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where code ='pos.order';"
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_purchase(self):
        to_removes = [
            # 清除采购单据
            ['purchase.order.line', ],
            ['purchase.order', ],
            ['purchase.requisition.line', ],
            ['purchase.requisition', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', '=', 'purchase.order')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where code ='purchase.order';"
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_mrp(self):
        to_removes = [
            # 清除生产单据
            ['mrp.workcenter.productivity', ],
            ['mrp.workorder', ],
            ['mrp.production.workcenter.line', ],
            ['change.production.qty', ],
            ['mrp.production', ],
            ['mrp.production.product.line', ],
            ['mrp.unbuild', ],
            ['change.production.qty', ],
            ['sale.forecast.indirect', ],
            ['sale.forecast', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
            seqs = self.env['ir.sequence'].search(['|', ('code', '=', 'mrp.production'), ('code', '=', 'mrp.unbuild')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where (code ='mrp.production' or code ='mrp.unbuild');"
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_mrp_bom(self):
        to_removes = [
            # 清除生产BOM
            ['mrp.bom.line', ],
            ['mrp.bom', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_inventory(self):
        to_removes = [
            # 清除库存单据
            ['stock.quant', ],
            ['stock.quant.package', ],
            ['stock.quant.move.rel', ],
            ['stock.move.line', ],
            ['stock.move', ],
            ['stock.pack.operation', ],
            ['stock.picking', ],
            ['stock.scrap', ],
            ['stock.inventory.line', ],
            ['stock.inventory', ],
            ['stock.production.lot', ],
            ['stock.fixed.putaway.strat', ],
            ['make.procurement', ],
            ['procurement.order', ],
            ['procurement.group', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
            seqs = self.env['ir.sequence'].search([
                '|', ('code', '=', 'stock.lot.serial'),
                '|', ('code', '=', 'stock.lot.tracking'),
                '|', ('code', '=', 'stock.orderpoint'),
                '|', ('code', '=', 'stock.picking'),
                '|', ('code', '=', 'stock.quant.package'),
                '|', ('code', '=', 'stock.scrap'),
                '|', ('code', '=', 'stock.picking'),
                '|', ('prefix', '=', 'WH/IN/'),
                '|', ('prefix', '=', 'WH/INT/'),
                '|', ('prefix', '=', 'WH/OUT/'),
                '|', ('prefix', '=', 'WH/PACK/'),
                ('prefix', '=', 'WH/PICK/')
            ])

            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            sql = "update ir_sequence set number_next=1 where (" \
                  "code ='stock.lot.serial' " \
                  "or code ='stock.lot.tracking' " \
                  "or code ='stock.orderpoint'" \
                  "or code ='stock.picking'" \
                  "or code ='stock.quant.package'" \
                  "or code ='stock.scrap'" \
                  "or code ='stock.picking'" \
                  "or prefix ='WH/IN/'" \
                  "or prefix ='WH/INT/'" \
                  "or prefix ='WH/OUT/'" \
                  "or prefix ='WH/PACK/'" \
                  "or prefix ='WH/PICK/'" \
                  ");"
            self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_account(self):
        to_removes = [
            # 清除财务会计单据
            ['account.voucher.line', ],
            ['account.voucher', ],
            ['account.bank.statement.line', ],
            ['account.bank.statement', ],
            ['account.payment', ],
            ['account.analytic.line', ],
            ['account.analytic.account', ],
            ['account.invoice.line', ],
            ['account.invoice.refund', ],
            ['account.invoice', ],
            ['account.partial.reconcile', ],
            ['account.move.line', ],
            ['hr.expense.sheet', ],
            ['account.move', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

                    # 更新序号
                    seqs = self.env['ir.sequence'].search([
                        '|', ('code', '=', 'account.reconcile'),
                        '|', ('code', '=', 'account.payment.customer.invoice'),
                        '|', ('code', '=', 'account.payment.customer.refund'),
                        '|', ('code', '=', 'account.payment.supplier.invoice'),
                        '|', ('code', '=', 'account.payment.supplier.refund'),
                        '|', ('code', '=', 'account.payment.transfer'),
                        '|', ('prefix', 'like', 'BNK1/'),
                        '|', ('prefix', 'like', 'CSH1/'),
                        '|', ('prefix', 'like', 'INV/'),
                        '|', ('prefix', 'like', 'EXCH/'),
                        '|', ('prefix', 'like', 'MISC/'),
                        '|', ('prefix', 'like', u'账单/'),
                        ('prefix', 'like', u'杂项/')
                    ])

                    for seq in seqs:
                        seq.write({
                            'number_next': 1,
                        })
                    # todo: 帐单 or BILL/%
                    sql = "update ir_sequence set number_next=1 where (" \
                          "code ='account.reconcile' " \
                          "or code ='account.payment.customer.invoice' " \
                          "or code ='account.payment.customer.refund' " \
                          "or code ='account.payment.supplier.invoice' " \
                          "or code ='account.payment.supplier.refund' " \
                          "or prefix like 'BNK1/%'" \
                          "or prefix like 'CSH1/%'" \
                          "or prefix like 'INV/%'" \
                          "or prefix like 'EXCH/%'" \
                          "or prefix like 'MISC/%'" \
                          "or prefix like '账单/%'" \
                          "or prefix like '杂项/%'" \
                          ");"
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_account_chart(self):
        to_removes = [
            # 清除财务科目，用于重设
            ['account.tax.account.tag', ],
            ['account.tax', ],
            ['account.account.account.tag', ],
            ['wizard_multi_charts_accounts'],
            ['account.account', ],
            ['account.journal', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

            # reset default tax，不管多公司
            field1 = self.env['ir.model.fields']._get('product.template', "taxes_id").id
            field2 = self.env['ir.model.fields']._get('product.template', "supplier_taxes_id").id

            sql = ("delete from ir_default where field_id = %s or field_id = %s") % (field1, field2)
            self._cr.execute(sql)

            sql = "update res_company set chart_template_id=null ;"
            self._cr.execute(sql)
            # 更新序号
        except Exception as e:
            pass
        return True

    @api.multi
    def remove_project(self):
        to_removes = [
            # 清除项目
            ['account.analytic.line', ],
            ['project.task', ],
            ['project.forecast', ],
            ['project.project', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
            # 更新序号
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_message(self):
        to_removes = [
            # 清除消息数据
            ['mail.message', ],
            ['mail.followers', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_workflow(self):
        to_removes = [
            # 清除工作流
            ['wkf.workitem', ],
            ['wkf.instance', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)

        except Exception as e:
            pass  # raise Warning(e)
        return True

    @api.multi
    def remove_all_biz(self):
        try:
            self.remove_account()
            self.remove_inventory()
            self.remove_mrp()
            self.remove_purchase()
            self.remove_sales()
            self.remove_project()
            self.remove_message()
        except Exception as e:
            pass  # raise Warning(e)
        return True
