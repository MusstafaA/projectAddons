from openerp import fields,models,api
from openerp import exceptions


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


    @api.multi
    def write(self, vals):
        vals;
        if 'delivery_id' in vals.keys():
            dman_record = self.env['pos.order'].search([('id', '=', vals['delivery_id'])])
            if dman_record['status'] == 'b':
                raise exceptions.ValidationError("Delivery man is busy now")
            else:
                dman_record['status'] = 'b'
        return super(Order, self).write(vals)


class Delivery(models.Model):
    _inherit="hr.employee"


    #==========================for test and will be restore======================
    # @api.one
    # def change_status(self):
    #     x = self.tyaar_state
    #     if x == 'a':
    #         self.tyaar_state = 'b'
    #         return self.tyaar_state
    #     elif x == 'b':
    #         self.tyaar_state = 'a'
    # ============================================================================

    # order_id = fields.Many2one('pos.order', string="orders")
    order_ids = fields.One2many("pos.order","delivery_id",select=True,string="Orders")
    # emp_code = fields.Char()
    tyaar_state = fields.Selection([('a', 'Available'), ('b', 'Busy')], 'Delivery Status')


