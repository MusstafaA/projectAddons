from openerp import fields,models,api
from openerp import exceptions


class Order(models.Model):
    _inherit="pos.order"
    delivery_id=fields.Many2one("hr.employee",string="Delivery Man")

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
    order_id = fields.One2many("pos.order","delivery_id",select=True,string="Orders")
    tyaar_state = fields.Selection([('a', 'Available'), ('b', 'Busy')], 'Delivery Status')

