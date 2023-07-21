from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
    ], ondelete={'motorcycle': 'set product'})

    type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle')
    ], ondelete={'motorcycle': 'set product'})
    
    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Char()
    charge_time = fields.Float()
    range1 = fields.Float()
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    year = fields.Integer()
    launch_date = fields.Date()