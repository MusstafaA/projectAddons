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





################ adding average function to res.partner model ##################

class PartnerInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    @api.one
    def _cal_average_usage(self):
        x = self.id
        partner_orders = self.env['pos.order'].search(
            [('partner_id', '=', x)])  # search_read([('partner_id', '=' , '32')], [])
        # total_prices_list = []

        total_prices_list = [ord['amount_total'] for ord in partner_orders]

        # for ord in partner_orders
        #     total_prices_list.append(ord['amount_total'])
        # length1 = len(partner_orders)
        length = len(total_prices_list)
        total = sum(total_prices_list)
        if length > 0:
            average = total / length
        else:
            average = 0.0

        return average


    partner_average_usage = fields.Float(compute=_cal_average_usage)
