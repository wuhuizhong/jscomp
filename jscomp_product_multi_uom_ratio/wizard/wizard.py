from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class WizTaskStockLines(models.TransientModel):
    _name = "wiz.uom.uom.line"
    wiz_id = fields.Many2one(string="uom_uom", comodel_name="wiz.uom.uom", )
    uom = fields.Char(string="Name", )
    utype = fields.Selection(
        string="Type",
        selection=[
            ('smaller', 'Smaller'),
            ('bigger', 'Bigger'),
        ],
        default='bigger'
    )
    qty = fields.Float(string="Ratio", digits=dp.get_precision('Product Unit of Measure'), )


class WizProdUoM(models.TransientModel):
    _name = 'wiz.uom.uom'

    line_ids = fields.One2many(string="UoMs", comodel_name="wiz.uom.uom.line", inverse_name="wiz_id", )
    ref_uom = fields.Char(string="Main UoM", )
    product_id = fields.Many2one(
        comodel_name='product.template', string='Product', select=True,
        default=lambda self: self.env.context.get('active_id', False))

    @property
    def create_uoms(self):
        product_id = self.product_id
        cat_name = product_id.name.replace(' ', '') + product_id.attr_spec.replace(' ', '') + '_uoms'
        existings = self.env['uom.category']._search([('name', '=', cat_name)])
        if existings:
            raise UserError(_('此产品已存在对应的计量单位组: %s，请在[设置]-[计量单位]里添加转换关系。') % cat_name)
        else:
            uom_categ_id = self.env['uom.category'].create({'name': cat_name})
            ref_uom_id = self.env['uom.uom'].create({
                'name': self.ref_uom,
                'uom_type': 'reference',
                'category_id': uom_categ_id.id,
                'rounding': 0.001,
                'factor': 1,
                'factor_inv': 1,
            })
            product_id.write({
                'uom_id': ref_uom_id.id,
                'uom_po_id': ref_uom_id.id,
            })
            for line in self.line_ids:
                self.env['uom.uom'].create({
                    'name': line.uom,
                    'uom_type': line.utype,
                    'factor_inv': line.utype == 'bigger' and abs(line.qty) or (1 / abs(line.qty)),
                    'factor': line.utype == 'smaller' and abs(line.qty),
                    'category_id': uom_categ_id.id,
                    'rounding': 0.001,
                })

        return True

    @api.multi
    def add_uoms(self):

        uom_ids = self.create_uoms

        return True
