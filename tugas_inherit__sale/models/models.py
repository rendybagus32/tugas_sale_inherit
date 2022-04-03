# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tugas_inherit__sale(models.Model):
#     _name = 'tugas_inherit__sale.tugas_inherit__sale'
#     _description = 'tugas_inherit__sale.tugas_inherit__sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
