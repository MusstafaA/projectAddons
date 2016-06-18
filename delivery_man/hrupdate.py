import re
from datetime import datetime

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
    delivery_man_id = fields.Many2one("hr.employee", string="Delivery Man")
    state = fields.Selection([('draft', 'New'),
                              ('out', 'Out for delivery'),
                              ('cancel', 'Cancelled'),
                              ('paid', 'Paid'),
                              ('done', 'Posted'),
                              ('invoiced', 'Invoiced')],
                              'Status', readonly=True)

    @api.multi
    def write(self, vals):
        if 'state' in vals.keys() and 'paid' in vals.values():
           if self[0].delivery_man_id :
            delivery_man_orders = self.env['pos.order'].search([('delivery_man_id', '=', self[0].delivery_man_id.id)])
            dman_record = self.env['hr.employee'].search([('id', '=', self[0].delivery_man_id.id)])
            dman_record['status'] = 'a'
            for order in delivery_man_orders:
                if order['id'] == self[0].id :
                   pass
                else:
                    if order['state'] == 'out':
                       dman_record['status'] = 'b'
        return super(OrderUpdate, self).write(vals)

class HrUpdate(models.Model):
    _inherit = "hr.employee"
    order_ids = fields.One2many("pos.order", "delivery_man_id", select=True, string="Orders")
    status = fields.Selection([('a', 'Avaliable'), ('b', 'Busy')], readonly=True, default='a')
    phone_ids = fields.One2many('delivery.phonenumbers', 'emp_id', string='phone numbers')
    mobile_ids = fields.One2many('delivery.mobilenumbers', 'emp_id', string='mobile numbers', required=True)
    address = fields.Char(string="Address")
    street = fields.Char(string='Street', required=True)
    city = fields.Char(string='City', required=True)
    state_id = fields.Many2one("res.country.state", string='State', required=True, ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', required=True)
    job_name = fields.Char(related='job_id.name',store=True)

    @api.model
    def create(self, values):
        pattern = re.compile("^[0-9]{6,10}$")
        pattern1 = re.compile("^[0-9]{11}$")
        pattern2 = re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                              + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
        if 'mobile_ids' in values.keys():
            for mobile in values['mobile_ids']:
                if mobile[2] != False:
                    if mobile[2]['mobile_nu'] != False:
                        if pattern1.match(mobile[2]['mobile_nu']):
                            pass
                        else:
                            raise exceptions.ValidationError("mobile numbers can only be integers must be  11 numbers")
                else:
                    raise exceptions.ValidationError("mobile numbers can only be integers must be  11 numbers")

        if 'phone_ids' in values.keys():
            for phone in values['phone_ids']:
                if phone[2] != False:
                    if phone[2]['phone_nu'] != False:
                        if pattern.match(phone[2]['phone_nu']):
                            pass

                        else:
                            raise exceptions.ValidationError("Phone  numbers can only be integers at least 6 numbers")
                    else:
                        raise exceptions.ValidationError("Phone  numbers can only be integers at least 6 numbers")

        if 'email' in values.keys():
            if pattern2.match(values['email']):
                pass
            else:
                raise exceptions.ValidationError("Not valid email address")

        return super(HrUpdate, self).create(values)

    @api.multi
    def write(self, values):
        values;
        pattern = re.compile("^[0-9]{6,10}$")
        pattern1 = re.compile("^[0-9]{11}$")
        pattern2 = re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                              + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
        pattern3 = re.compile("^[0-9]{14}$")
        if  'work_phone' in values.keys():
            if pattern.match(values['work_phone']):
               pass
            else:
                raise exceptions.ValidationError("Work Phone  number can only be integers at least 6 numbers")

        if 'mobile_phone' in values.keys():
            if pattern1.match(values['mobile_phone']):
                pass
            else:
                raise exceptions.ValidationError("Work Mobile Phone  number can only be integers must be  11 numbers")
        if 'work_email' in values.keys():
            if pattern2.match(values['work_email']):
                pass
            else:
                raise exceptions.ValidationError("Not valid email address")

        if 'identification_id' in values.keys():
            if pattern3.match(values['identification_id']):
                pass
            else:
                raise exceptions.ValidationError("Identification Number must be 10 numbers")

        if 'mobile_ids' in values.keys():
            for mobile in values['mobile_ids']:
                if mobile[2] != False:
                    if mobile[2]['mobile_nu'] != False:
                        if pattern1.match(mobile[2]['mobile_nu']):
                            pass
                        else:
                            raise exceptions.ValidationError("mobile numbers can only be integers must be  11 numbers")
                else:
                    raise exceptions.ValidationError("mobile numbers can only be integers must be  11 numbers")

        if 'phone_ids' in values.keys():
            for phone in values['phone_ids']:
                if phone[2] != False:
                    if phone[2]['phone_nu'] != False:
                        if pattern.match(phone[2]['phone_nu']):
                            pass

                        else:
                            raise exceptions.ValidationError("Phone  numbers can only be integers at least 6 numbers")
                    else:
                        raise exceptions.ValidationError("Phone  numbers can only be integers at least 6 numbers")

        if 'email' in values.keys():
            if pattern2.match(values['email']):
                pass
            else:
                raise exceptions.ValidationError("Not valid email address")

        if 'order_ids' in values.keys():

            delivery_man_orders = self.env['pos.order'].search([('delivery_man_id', '=', self[0].id)])
            dman_record = self.env['hr.employee'].search([('id', '=', self[0].id)])
            for order in delivery_man_orders:
                if order['state'] == 'out':
                    raise exceptions.ValidationError("Delivery Man is busy now")

            for order in values['order_ids']:
                order_record = self.env['pos.order'].search([('id', '=', order[1])])
                if order_record['state'] == 'draft':
                    order_record['state'] = 'out'
                    dman_record['status'] = 'b'
        return super(HrUpdate, self).write(values)


