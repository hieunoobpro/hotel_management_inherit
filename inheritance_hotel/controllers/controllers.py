# -*- coding: utf-8 -*-
# from odoo import http


# class InheritanceHotel(http.Controller):
#     @http.route('/inheritance_hotel/inheritance_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inheritance_hotel/inheritance_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inheritance_hotel.listing', {
#             'root': '/inheritance_hotel/inheritance_hotel',
#             'objects': http.request.env['inheritance_hotel.inheritance_hotel'].search([]),
#         })

#     @http.route('/inheritance_hotel/inheritance_hotel/objects/<model("inheritance_hotel.inheritance_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inheritance_hotel.object', {
#             'object': obj
#         })

