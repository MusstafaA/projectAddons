from openerp import fields,models,api


class Order(models.Model):
    _inherit="pos.order"

    # @api.one
    # def change_status(self):
    #     x = self.tyaar_state
    #     if x == 'a':
    #         self.tyaar_state = 'b'
    #         return self.tyaar_state
    #     elif x == 'b':
    #         self.tyaar_state = 'a'


    delivery_id=fields.Many2one("hr.employee",string="Delivery")
    tyaar_state = fields.Selection([('a','Available'),('b','Busy')],'Delivery Status')


class Delivery(models.Model):
    _inherit="hr.employee"

    @api.one
    def change_status(self):
        x = self.tyaar_state
        if x == 'a':
            self.tyaar_state = 'b'
            return self.tyaar_state
        elif x == 'b':
            self.tyaar_state = 'a'

    # order_id = fields.Many2one('pos.order', string="orders")
    order_ids = fields.One2many("pos.order","delivery_id",select=True,string="Orders")
    # emp_code = fields.Char()
    tyaar_state = fields.Selection([('a', 'Available'), ('b', 'Busy')], 'Delivery Status')

