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

from odoo import _, api, fields, models


class ProductCustomerCode(models.Model):
    _name = "product.customer.code"
    _description = "Add Code and Name of customer's product"
    _rec_name = 'product_code'

    product_code = fields.Char(string='Customer Product Code', help="""This
        customer's product code will be used when searching into a request for
        quotation.""")
    product_name = fields.Char(string='Customer Product Name', help="""This
        customer's product name will be used when searching into a request for
        quotation.""")
    product_id = fields.Many2one('product.template', string='Product Template',
        required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    company_id = fields.Many2one('res.company', string='Company', required=False,
        default=lambda self: self.env.user.company_id)

    _sql_constraints = [
        ('unique_code', 'unique(product_code, company_id, partner_id)',
         'Product Code of customer must be unique'),
    ]
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: