import collections
from openerp import models, fields, api
from operator import itemgetter, attrgetter, methodcaller


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
		words = []
		words.append(products)
		word_counts = collections.Counter(words)
		counter = 0
		product = {}
		for word, count in sorted(word_counts.items()):
    	# print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
			product[counter] = {
						'name':word,
						'count':count
    							}
			counter = counter + 1
		values = product.values()
		newlist = sorted(values, key=lambda k: k['count'], reverse=True)
		#this will return a sorted list of dictionary
		print newlist	
		#print products

# It is just a temporary test to add something
class ResPartnerInherit(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Partner'


	all_orders = fields.One2many('pos.order', 'partner_id', string='All Orders')
