from odoo import http

class Kawiil(http.Controller):
    @http.route('/compare/', auth='public', website=True)
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        return http.request.render('kawiil.motorcycle_comparation',{
            'motorcycles': motorcycles
        })
    
    """"
    @http.route('route/subroute/', auth='public', website=True)
    def subroute(self, **kw):
        subroutes = http.request.env['motorcycle.registry'].search([])
        return http.request.render('motorcycle.motorcycles_website',{
            'registry': subroutes,
        })
    """