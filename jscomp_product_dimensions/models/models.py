# -*- coding: utf-8 -*-
from math import ceil
from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    attr_draw_no = fields.Char(string="Draw No.")
    attr_spec = fields.Char(string="Specification")
    attr_diameter = fields.Float(string="Diameter (mm)", digits=dp.get_precision('Product Unit of Measure'),
                                 help="In mm", default=0.0)
    attr_thickness = fields.Float(string="Thickness(mm)", digits=dp.get_precision('Product Unit of Measure'),
                                  help="In mm", default=0.0)
    attr_length = fields.Float(string="Length (mm)", digits=dp.get_precision('Product Unit of Measure'), help="In mm",
                               default=0.0)
    attr_weight = fields.Float(string="Weight (Kg)", digits=dp.get_precision('Product Unit of Measure'),
                               compute="_compute_prod_weight", store=1, readonly=1)

    @api.depends('attr_diameter', 'attr_thickness', 'attr_length')
    def _compute_prod_weight(self):
        for prod in self:
            if prod.attr_diameter > 0 and prod.attr_thickness > 0 and prod.attr_length > 0:
                prod.attr_weight = 3.1416 * (prod.attr_diameter ** 2 - (
                        prod.attr_diameter - prod.attr_thickness * 2) ** 2) / 4 * prod.attr_length / 1000000 * 7.85

    @api.multi
    def name_get(self):
        return [(template.id, '%s%s%s' % (
            (template.default_code and '[%s] ' % template.default_code or ''), template.name,
            (template.attr_spec and '%s' % template.attr_spec or '')))
                for template in self]


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    attr_draw_no = fields.Char(related="product_id.attr_draw_no", readonly=1)
    attr_spec = fields.Char(related="product_id.attr_spec", readonly=1)
    attr_diameter = fields.Float(related="product_id.attr_diameter", readonly=1)
    attr_thickness = fields.Float(related="product_id.attr_thickness", readonly=1)
    attr_length = fields.Float(related="product_id.attr_length", readonly=1)
    attr_weight = fields.Float(related="product_id.attr_weight", readonly=1)
    request_qty = fields.Float("Req. Qty", help="Requested qty for Dimension calculation")

    @api.onchange('request_qty', 'product_uom', 'product_id')
    def _calc_dimension_qty(self):
        if self.attr_weight > 0.0:
            self.product_qty = self.request_qty * self.product_uom.factor
        else:
            self.request_qty = 0


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    attr_draw_no = fields.Char(related="product_id.attr_draw_no", readonly=1)
    attr_spec = fields.Char(related="product_id.attr_spec", readonly=1)
    attr_diameter = fields.Float(related="product_id.attr_diameter", readonly=1)
    attr_thickness = fields.Float(related="product_id.attr_thickness", readonly=1)
    attr_length = fields.Float(related="product_id.attr_length", readonly=1)
    attr_weight = fields.Float(related="product_id.attr_weight", readonly=1)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    _sql_constraints = [
        ('default_code_uniq', 'unique(default_code)', "A default_code can only be assigned to one product !"),
    ]

    @api.multi
    def name_get(self):
        # TDE: this could be cleaned a bit I think

        def _name_get(d):

            name = '%s%s' %(d.get('name', ''), d.get('spec', ''))
            code = self._context.get('display_default_code', True) and d.get('default_code', False) or False
            if code:
                name = '[%s] %s' % (code, name)
            return (d['id'], name)

        partner_id = self._context.get('partner_id')
        if partner_id:
            partner_ids = [partner_id, self.env['res.partner'].browse(partner_id).commercial_partner_id.id]
        else:
            partner_ids = []

        # all user don't have access to seller and partner
        # check access and use superuser
        self.check_access_rights("read")
        self.check_access_rule("read")

        result = []
        for product in self.sudo():
            # display only the attributes with multiple possible values on the template
            variable_attributes = product.attribute_line_ids.filtered(lambda l: len(l.value_ids) > 1).mapped(
                'attribute_id')
            variant = product.attribute_value_ids._variant_name(variable_attributes)

            name = variant and "%s(%s)" % (product.name, variant) or product.name
            sellers = []
            if partner_ids:
                sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and (x.product_id == product)]
                if not sellers:
                    sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and not x.product_id]
            if sellers:
                for s in sellers:
                    seller_variant = s.product_name and (
                            variant and "%s(%s)" % (s.product_name, variant) or s.product_name
                    ) or False
                    mydict = {
                        'id': product.id,
                        'name': seller_variant or name,
                        'spec': product.attr_spec or '',
                        'default_code': s.product_code or product.default_code,
                    }
                    temp = _name_get(mydict)
                    if temp not in result:
                        result.append(temp)
            else:
                mydict = {
                    'id': product.id,
                    'name': name,
                    'spec': product.attr_spec or '',
                    'default_code': product.default_code,
                }
                result.append(_name_get(mydict))
        return result
