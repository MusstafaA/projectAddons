#this is the model inhertience

from openerp import models, fields

#add a new relationship to phone numbers and mobile numbers
class PhoneNumbers(models.Model):
	_name = 'customer.phonenumbers'
	phone_num = fields.Integer(size=64, string="Phone Numbers")
	partner_id = fields.Many2one('res.partner',string='Customer Name')


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
	#order_ids = fields.One2many('pos.order', 'partner_id', string='Latest Order', limit=1)

    

class CustTags(models.Model):
	_name= 'cust.tags'
	name = fields.Char()		