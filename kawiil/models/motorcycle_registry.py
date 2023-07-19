from odoo import models, fields

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _rec_name = 'registry_number'

    registry_number = fields.Char(required=True)
    vin = fields.Char(requiered=True)
    first_name = fields.Char(requiered=True)
    last_name = fields.Char(requiered=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()