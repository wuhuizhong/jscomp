# -*- coding: utf-8 -*-
###############################################################################
#
#   customer_product_code for Odoo
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import _, api, fields, models, SUPERUSER_ID


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _order = "default_code, name"

    product_customer_code_ids = fields.One2many('product.customer.code',
        'product_id', 'Customer Codes')
    default_code = fields.Char(related='product_variant_ids.default_code',
        string='Internal Reference', store=True)

class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _product_partner_ref(self):
        res = {}
        for p in self:
            data = self._get_partner_code_name(p, self._context.get('partner_id', None))
            if not data['code']:
                data['code'] = p.code
            if not data['name']:
                data['name'] = p.name
            res[p.id] = (data['code'] and ('['+data['code']+'] ') or '') + (data['name'] or '')
            p.partner_ref = res[p.id]
        return res
# 
    @api.multi
    def _get_partner_code_name(self, product, partner_id):
        if self._context.get('type', False) == 'in_invoice':
            for supinfo in product.seller_ids:
                if supinfo.name.id == partner_id:
                    return {'code': supinfo.product_code or product.default_code, 'name': supinfo.product_name or product.name}
        else:
            for buyinfo in product.product_customer_code_ids:
                if buyinfo.partner_id.id == partner_id:
                    return {'code': buyinfo.product_code or product.default_code, 'name': buyinfo.product_name or product.name}
        res = {'code': product.default_code, 'name': product.name}
        return res
 
    partner_ref = fields.Char(compute='_product_partner_ref', string='Customer ref')

    @api.multi
    def copy(self, default=None):
        if not default:
            default = {}
        default['product_customer_code_ids'] = False
        res = super(ProductProduct, self).copy(default=default)
        return res

    @api.multi
    def name_get(self):
#         # TDE: this could be cleaned a bit I think
# 
        def _name_get(d):
            name = d.get('name', '')
            code = self._context.get('display_default_code', True) and d.get('default_code', False) or False
            base_product = self.browse(d.get('id')) or False
            if code:
                if self._context.get('type', False) == 'out_invoice' and base_product and not d.get('has_customer'):
                    name = '[%s] %s' % (base_product.default_code, base_product.name)
                else:
                   name = '[%s] %s' % (code, name)
            return (d['id'], name)
 
        partner_id = self._context.get('partner_id')
        if partner_id:
            partner_ids = [partner_id, self.env['res.partner'].browse(partner_id).commercial_partner_id.id]
        else:
            partner_ids = []
# 
#         # all user don't have access to seller and partner
#         # check access and use superuser
        self.check_access_rights("read")
        self.check_access_rule("read")
 
        result = []
        for product in self.sudo():
            # display only the attributes with multiple possible values on the template
            variable_attributes = product.attribute_line_ids.filtered(lambda l: len(l.value_ids) > 1).mapped('attribute_id')
            variant = product.attribute_value_ids._variant_name(variable_attributes)
 
            name = variant and "%s (%s)" % (product.name, variant) or product.name
            sellers = []
            buyers = []
            if partner_ids:
                sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and (x.product_id == product)]
                if not sellers:
                    sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and not x.product_id]
                buyers = [x for x in product.product_customer_code_ids if (x.partner_id.id == partner_id) and (x.product_id == product.product_tmpl_id)]
                if not buyers:
                    buyers = [x for x in product.product_customer_code_ids if (x.partner_id.id == partner_id) and not x.product_id.product_tmpl_id]
            if sellers:
                for s in sellers:
                    seller_variant = s.product_name and (
                        variant and "%s (%s)" % (s.product_name, variant) or s.product_name
                        ) or False
                    mydict = {
                              'id': product.id,
                              'name': seller_variant or name,
                              'default_code': s.product_code or product.default_code,
                              }
                    temp = _name_get(mydict)
                    if temp not in result:
                        result.append(temp)
            elif buyers:
                for b in buyers:
                    mydict = {
                              'id': product.id,
                              'name': b.product_name or product.name,
                              'default_code': b.product_code or product.default_code,
                              'product_obj': product,
                              'has_customer': True
                              }
                    result.append(_name_get(mydict))
            else:
                mydict = {
                          'id': product.id,
                          'name': name,
                          'default_code': product.default_code,
                          }
                result.append(_name_get(mydict))
        return result
   
    @api.model
    def name_search(self, name='', args=None, operator='ilike',limit=80):
        if not args:
            args = []
        res = super(ProductProduct, self).name_search(name, args=args,
            operator=operator, limit=limit)
        if not self._context:
            context = {}
        product_customer_code_obj = self.env['product.customer.code']
        if not res:
            ids = []
            partner_id = self._context.get('partner_id', False)
            if partner_id:
                id_prod_code = product_customer_code_obj.search([
                    ('product_code', '=', name), ('partner_id', '=', partner_id)
                    ], limit=limit)
                 
                for ppu in id_prod_code:
                    ids.append(ppu.product_id.id)
            if ids:
                res = self.name_get()
        return res