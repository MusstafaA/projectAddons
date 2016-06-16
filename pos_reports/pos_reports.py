import collections
from openerp import models, fields, api
from operator import itemgetter, attrgetter, methodcaller

# all_length = 0

class HrsEmployeeInherit(models.Model):
    #to link the model in the other Module Hr
	_inherit = 'pos.order'
	
	# @api.one
	# def get_length(self, length):
	# 	global all_length
	# 	all_length += length
	# 	print all_length			

class OrderLineInherit(models.Model):
    #to link the model in the other Module Hr
	all_products = []
	all_length = 0
	_inherit = 'pos.order.line'

	@api.one
	def get_products(self, products, length):
		for x in xrange(0,length):
			OrderLineInherit.all_products.append(products)
		if len(OrderLineInherit.all_products) == OrderLineInherit.all_length:
			# print OrderLineInherit.all_products
			
			word_counts = collections.Counter(OrderLineInherit.all_products)
			counter = 0
			product = {}
			for word, count in sorted(word_counts.items()):
				product[counter] = {
							'name':word,
							'count':count
	    							}
				counter = counter + 1
			values = product.values()
			newlist = sorted(values, key=lambda k: k['count'], reverse=True)
			#this will return a sorted list of dictionary
			# print products
			OrderLineInherit.all_products = []
			OrderLineInherit.all_length = 0
			return newlist	

	@api.one
	def get_length(self, length):
		OrderLineInherit.all_length += length
		# print OrderLineInherit.all_length	

# It is just a temporary test to add something
class ResPartnerInherit(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Partner'


	all_orders = fields.One2many('pos.order', 'partner_id', string='All Orders')
