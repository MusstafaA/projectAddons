from openerp import models, fields


class KitchenOrders(models.Model):
    _inherit = 'pos.order'
    _name = "pos.order"

    stage = fields.Selection([('kitchen', 'In Kitchen'),('Delivery', 'Out for Delivery'),('Delivered', 'Delivered')],'Current Stage', default= 'kitchen' ,readonly=False, copy=False)




