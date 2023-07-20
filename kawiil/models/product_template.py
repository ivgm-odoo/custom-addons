from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], ondelete={'motorcycle': 'set product'})