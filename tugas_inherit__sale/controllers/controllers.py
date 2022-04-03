# -*- coding: utf-8 -*-
# from odoo import http


# class TugasInheritSale(http.Controller):
#     @http.route('/tugas_inherit__sale/tugas_inherit__sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tugas_inherit__sale/tugas_inherit__sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tugas_inherit__sale.listing', {
#             'root': '/tugas_inherit__sale/tugas_inherit__sale',
#             'objects': http.request.env['tugas_inherit__sale.tugas_inherit__sale'].search([]),
#         })

#     @http.route('/tugas_inherit__sale/tugas_inherit__sale/objects/<model("tugas_inherit__sale.tugas_inherit__sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tugas_inherit__sale.object', {
#             'object': obj
#         })
