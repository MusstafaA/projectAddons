from openerp import models, fields

class HrsEmployeeInherit(models.Model):
    #to link the model in the other Module Hr
    _inherit = 'pos.order'



# It is just a temporary test to add something
class ResPartnerInherit(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Partner'


	all_orders = fields.One2many('pos.order', 'partner_id', string='All Orders')
