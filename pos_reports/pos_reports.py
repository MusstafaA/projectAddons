from openerp import models, fields, api

class HrsEmployeeInherit(models.Model):
    #to link the model in the other Module Hr
	_inherit = 'pos.order'
	
	@api.one
	def get_products(self, products):
		for x in products:
			print x
				

class OrderLineInherit(models.Model):
    #to link the model in the other Module Hr
	_inherit = 'pos.order.line'
	
	@api.one
	def get_products(self, products):
		print products

# It is just a temporary test to add something
class ResPartnerInherit(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Partner'


	all_orders = fields.One2many('pos.order', 'partner_id', string='All Orders')
