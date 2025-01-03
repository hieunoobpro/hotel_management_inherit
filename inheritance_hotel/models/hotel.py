from odoo import models, fields

class HotelManagementInherit(models.Model):
    _inherit = 'hotel.management'

    booking_history_ids = fields.One2many('room.booking', 'hotel_id', string="Booking History")
