from odoo import models, fields
class BookingHistory(models.Model):
    _name = 'booking.history'
    _description = 'Booking History'
    _inherit = 'room.booking'

    hotel_id = fields.Many2one('hotel.management', string='Hotel', required=True)


