# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    print_image = fields.Boolean(
        'Print Image', help="""If ticked, you can see the product image in
        report of sale order/quotation""")
    print_desc = fields.Boolean("Print Description", default=True)
    image_sizes = fields.Selection(
        [('image', 'Big sized Image'), ('image_medium', 'Medium Sized Image'),
         ('image_small', 'Small Sized Image')],
        'Image Sizes', default="image_small",
        help="Image size to be displayed in report")



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    image_small = fields.Binary( 'Product Image', related='product_id.image_small')
   # prod_desc = fields.Text('Product Description', related='product_id.prod_desc')
