# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Notes
        """
        if not self.partner_id:
            self.notes = False
        else:
            # self.notes = self.with_context(lang=self.partner_id.lang).env['res.partner'].browse(self.partner_id.id).comment
            self.notes = self.env['res.partner'].browse(self.partner_id.id).comment

        return super(PurchaseOrder, self).onchange_partner_id()
