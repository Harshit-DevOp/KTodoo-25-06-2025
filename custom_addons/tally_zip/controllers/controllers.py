# -*- coding: utf-8 -*-
# from odoo import http


# class TallyZip(http.Controller):
#     @http.route('/tally_zip/tally_zip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tally_zip/tally_zip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tally_zip.listing', {
#             'root': '/tally_zip/tally_zip',
#             'objects': http.request.env['tally_zip.tally_zip'].search([]),
#         })

#     @http.route('/tally_zip/tally_zip/objects/<model("tally_zip.tally_zip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tally_zip.object', {
#             'object': obj
#         })

