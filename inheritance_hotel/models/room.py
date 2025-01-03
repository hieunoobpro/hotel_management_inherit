from odoo import models, fields

class RoomManagementInherit(models.Model):
    _inherit = 'room.management'

    room_size = fields.Selection(
        [('small', 'Small'), 
         ('medium', 'Medium'), 
         ('large', 'Large'), 
         ('president', 'President')], 
        string="Room Size"
    )
    max_occupancy = fields.Integer(string="Max Occupancy")
    smoking_allowed = fields.Selection(
        [('yes', 'Yes'), ('no', 'No')], 
        string="Smoking Allowed", 
        default='no'
    )