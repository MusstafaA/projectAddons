#this is the model inhertience

from openerp import models, fields, api

#Functions.....................
@api.multi
def _average_amount(self):
	return self.env.user


#..........................
#add a new relationship to phone numbers and mobile numbers
class PhoneNumbers(models.Model):
	_name = 'customer.phonenumbers'
	phone_num = fields.Integer(size=64, string="Phone Numbers")
	partner_id = fields.Many2one('res.partner',string='Customer Name')

	def phones_from_ui(self, cr, uid, partner, context=None):
		""" create or modify a partner from the point of sale ui.
			partner contains the partner's fields. """
		self.create(cr, uid, partner, context=None)						


class MobileNumbers(models.Model):
	_name = 'customer.mobilenumbers'
	mobile_num = fields.Integer(size=64, string="Mobile Numbers")
	partner_id = fields.Many2one('res.partner', string='Customer Name')


class ResPartnerInherit(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Partner'
	#One2many -> Logical remmber !
	phone_ids = fields.One2many('customer.phonenumbers', 'partner_id', string='Phone Numbers')
	mobile_ids = fields.One2many('customer.mobilenumbers', 'partner_id', string='Mobile Numbers')	
	tags_ids = fields.Many2many('cust.tags',string="Tags")
	other_address = fields.Char(string="Other Address")
	street_2 = fields.Char(string='Street 2')
	zip_2 = fields.Char(string='Zip 2', size=24, change_default=True)
	city_2  = fields.Char(string='City 2')
	state_id_2 = fields.Many2one("res.country.state", string='State 2', ondelete='restrict')
	country_id_2 =  fields.Many2one('res.country', string='Country 2', ondelete='restrict')
	order_ids = fields.One2many('pos.order', 'partner_id', string='Latest Order', limit=1)
	order_average_ids = fields.One2many('pos.order', 'partner_id', string='All Orders')



class CustTags(models.Model):
	_name= 'cust.tags'
	name = fields.Char()





# class PosOrderInherit(models.Model):
#  	_name = 'pos.order'
#  	_inherit = 'pos.order'
#  	_description = 'Order'


# 	@api.multi
# 	def _average_amount(self):
# 		for record in self:
# 			record.order_average = record.order_average + record.amount_total
# 		return True
	
#  	order_average = fields.Float(compute=_average_amount)


			