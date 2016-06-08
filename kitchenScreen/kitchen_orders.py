from openerp import models, fields,api


class KitchenOrders(models.Model):
    _inherit = 'pos.order'
    _name = "pos.order"

    @api.one
    def change_stage(self):
        x = self.stage
        if x == 'kitchen' :
            self.stage = 'Ready for delivery'
            return self.stage
        elif x == 'Ready for delivery':
            self.stage = 'Delivery'
        elif x == 'Delivery' :
            self.stage = 'Delivered'
        else:
            self.stage = 'kitchen'



    stage = fields.Selection([('kitchen', 'In Kitchen'),('Ready for delivery', 'Ready for Delivery'),('Delivery', 'Out for Delivery'),('Delivered', 'Delivered')],'Current Stage', default= 'kitchen' ,readonly=False, copy=False)




