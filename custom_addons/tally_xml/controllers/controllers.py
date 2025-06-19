# -*- coding: utf-8 -*-
# from odoo import http


# class TallyXml(http.Controller):
#     @http.route('/tally_xml/tally_xml', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tally_xml/tally_xml/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tally_xml.listing', {
#             'root': '/tally_xml/tally_xml',
#             'objects': http.request.env['tally_xml.tally_xml'].search([]),
#         })

#     @http.route('/tally_xml/tally_xml/objects/<model("tally_xml.tally_xml"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tally_xml.object', {
#             'object': obj
#         })

