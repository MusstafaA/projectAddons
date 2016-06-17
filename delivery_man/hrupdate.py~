import re

from openerp import models ,fields , api ,exceptions


class PhoneNumbers(models.Model):
    _name = 'delivery.phonenumbers'
    phone_nu = fields.Char(string='Phone numbers')
    emp_id = fields.Many2one('hr.employee')


class MobileNumbers(models.Model):
    _name = 'delivery.mobilenumbers'
    mobile_nu = fields.Char(string='Mobile numbers')
    emp_id    =    fields.Many2one('hr.employee')

class OrderUpdate(models.Model):
    _inherit = 'pos.order'
    # delivery_man_id=fields.Many2one('project.delivery')
    state = fields.Selection([('draft', 'New'),
                              ('out', 'Out for delivery'),
                              ('cancel', 'Cancelled'),
                              ('paid', 'Paid'),
                              ('done', 'Posted'),
                              ('invoiced', 'Invoiced')],
                              'Status', readonly=True)

    @api.multi
    def write(self, vals):
        vals;
        if 'state' in vals.keys() and 'paid' in vals.values():
            delivery_man_orders = self.env['pos.order'].search([('delivery_man_id', '=', self[0].delivery_man_id.id)])
            dman_record = self.env['hr.employee'].search([('id', '=', self[0].delivery_man_id.id)])
            dman_record['status'] = 'a'
            for order in delivery_man_orders:
                if order['state'] == 'out':
                   dman_record['status'] = 'b'
        return super(OrderUpdate, self).write(vals)


