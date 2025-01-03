from odoo import models, fields

class InheritedRoomFeature(models.Model):
    _inherit = 'room.feature'

    # Add your custom fields or methods here
    additional_feature = fields.Char(string='Additional Feature')