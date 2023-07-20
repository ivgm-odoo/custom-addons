from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _rec_name = 'registry_number'
    _sql_constraints = [('unique_vin', 'unique(vin)', 'The VIN must be unique.'),]

    registry_number = fields.Char(string="Motorcycle Registry Number", required=True, default="MRN0001", copy=False, readonly=True)
    vin = fields.Char(required=True)
    #first_name = fields.Char(required=True)
    #last_name = fields.Char(required=True)
    owner = fields.Many2one(comodel_name="res.partner", string="Partner", ondelete="cascade")
    email = fields.Char(related="owner.email")
    phone = fields.Char(related="owner.phone")
    make = fields.Char(string="Make", compute="_compute_make")
    model = fields.Char(string="Model", compute="_compute_model")
    year = fields.Char(string="Year", compute="_compute_year")
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        for registry in self:
            validate = re.search('^[A-Z]{4}[0-9]{2}[0-9A-Z]{2}[0-9]{6}$', registry.vin)
            if(not validate):
                raise ValidationError('The VIN does not meet the definition rules')

    @api.constrains('license_plate')
    def _check_license_plate(self):
        for registry in self:
            validate = re.search("^[A-Z]{1,4}[0-9]{1,3}[A-Z]{0,2}$", registry.license_plate)
            if(not validate):
                raise ValidationError('The License Plate does not meet the definition rules')
            
    @api.depends('vin')
    def _compute_make(self):
        for rec in self: 
            rec.make = "" if rec.vin==False else rec.vin[0:2]

    @api.depends('vin')
    def _compute_model(self):
        for rec in self: 
            rec.model = "" if rec.vin==False else rec.vin[2:4]

    @api.depends('vin')
    def _compute_year(self):
        for rec in self: 
            rec.year = "" if rec.vin==False else rec.vin[4:6]
