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
        # elif x == 'Ready for delivery':
        #     self.stage = 'Delivery'
        # elif x == 'Delivery' :
        #     self.stage = 'Delivered'
        # else:
        #     self.stage = 'kitchen'



    stage = fields.Selection([('kitchen', 'In Kitchen'),('Ready for delivery', 'Ready for Delivery'),('Delivery', 'Out for Delivery'),('Delivered', 'Delivered')],'Current Stage', default= 'kitchen' ,readonly=False, copy=False)
    zone = fields.Selection([('A', 'Area A'), ('B', 'Area B'), ('C', 'Area C'),('D', 'Area D')], 'Zone')

    @api.one
    def order_line_get(self):
        # result = self
        result = []
        self._cr.execute('SELECT * FROM pos_order_line WHERE order_id=%s', (self.id,))

        # result = cr.dictfetchall()
        for t in self._cr.dictfetchall():
            result.append(t)
            # result.append({
                # 'name': t['name'],
                # 'lines': t['lines'],
                # 'price': t['amount'] or 0.0,
                # 'account_id': t['account_id'],
                # 'tax_code_id': t['tax_code_id'],
                # 'tax_amount': t['tax_amount'],
                # 'account_analytic_id': t['account_analytic_id'],
            # })
        return result

# class ParticularReport(models.AbstractModel):
#     _name = 'report.module.report_name'
#     @api.multi
#     def render_html(self, data=None):
#         report_obj = self.env['report']
#         report = report_obj._get_report_from_name('module.report_name')
#         docargs = {
#             'doc_ids': self._ids,
#             'doc_model': report.model,
#             'docs': self,
#         }
#         return report_obj.render('module.report_name', docargs)



################ adding average function to res.partner model ##################

class PartnerInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    @api.multi
    def _cal_average_usage(self):
        users = []
        for user in self :
            users.append(user)

        for partner in users :
            x = partner.id
            partner_orders = self.env['pos.order'].search([('partner_id', '=', x)])  # search_read([('partner_id', '=' , '32')], [])
            # total_prices_list = []

            total_prices_list = [ord['amount_total'] for ord in partner_orders]

            # for ord in partner_orders
            #     total_prices_list.append(ord['amount_total'])
            # length1 = len(partner_orders)
            length = len(total_prices_list)
            total = sum(total_prices_list)
            if length > 0:
                partner.partner_average_usage = total / length
            else:
                partner.partner_average_usage  = 0.0




    partner_average_usage = fields.Float(compute=_cal_average_usage)



