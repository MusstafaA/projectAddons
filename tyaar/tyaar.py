from openerp import fields,models,api


# class delivery(models.Model):
#     _name = "iti.delivery"
#
#     name=fields.Char()


class Order(models.Model):
    _inherit="pos.order"

#     delivery_id=fields.Many2one("hr.employee",string="Delivery")



class Delivery(models.Model):
    _inherit="hr.employee"

    order_id = fields.Many2one('pos.order', string="orders")


