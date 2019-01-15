# -*- coding: utf-8 -*-
from odoo import http

# class Modules(http.Controller):
#     @http.route('/modules/modules/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modules/modules/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modules.listing', {
#             'root': '/modules/modules',
#             'objects': http.request.env['modules.modules'].search([]),
#         })

#     @http.route('/modules/modules/objects/<model("modules.modules"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modules.object', {
#             'object': obj
#         })