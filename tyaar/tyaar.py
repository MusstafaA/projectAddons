from openerp import fields,models,api


class Order(models.Model):
    _inherit="pos.order"

    delivery_id=fields.Many2one("hr.employee",string="Delivery")



class Delivery(models.Model):
    _inherit="hr.employee"

    # order_id = fields.Many2one('pos.order', string="orders")
    order_ids = fields.One2many("pos.order","delivery_id",string="Orders")


