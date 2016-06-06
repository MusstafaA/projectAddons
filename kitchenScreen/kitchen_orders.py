from openerp import models, fields,api


class KitchenOrders(models.Model):
    _inherit = 'pos.order'
    _name = "pos.order"

    @api.one
    def change_stage(self):
        x = self.stage
        if x == 'kitchen' :
            self.stage = 'Delivery'
            return self.stage
        elif x == 'Delivery' :
            self.stage = 'Delivered'
        else:
            self.stage = 'kitchen'



    stage = fields.Selection([('kitchen', 'In Kitchen'),('Delivery', 'Out for Delivery'),('Delivered', 'Delivered')],'Current Stage', default= 'kitchen' ,readonly=False, copy=False)




