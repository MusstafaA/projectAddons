import re

from openerp import models ,fields , api ,exceptions


class PhoneNumbers(models.Model):
        _name='project.phonenumbers'
        phone_nu=fields.Text(string='Phone numbers')
        partner_id = fields.Many2one('res.partner')


class MobileNumbers(models.Model):
        _name = 'project.mobilenumbers'
        mobile_nu = fields.Text(string='Mobile numbers')
        partner_id=fields.Many2one('res.partner')

class OrderUpdate(models.Model):
        _inherit='pos.order'
        delivery_man_id=fields.Many2one('project.delivery')
        state= fields.Selection([('draft', 'New'),
                                  ('out', 'Out for delivery'),
                                   ('cancel', 'Cancelled'),
                                   ('paid', 'Paid'),
                                   ('done', 'Posted'),
                                   ('invoiced', 'Invoiced')],
                                  'Status', readonly=True)
        @api.multi
        def write(self, vals):
            if 'delivery_man_id' in vals.keys():
                 dman_record = self.env['project.delivery'].search([('id', '=', vals['delivery_man_id'])])
                 if  dman_record['status']== 'b':
                     raise exceptions.ValidationError("Delivery man is busy now")
                 else:
                     dman_record['status']='b'
            return super(OrderUpdate, self).write(vals)



class delivery(models.Model):
      _name='project.delivery'
      name = fields.Char(required=True)
      email=fields.Char(required=True)
      image = fields.Binary()
      date_of_birth = fields.Date(required=True)
      phone_ids =  fields.One2many('project.phonenumbers', 'partner_id', string='phone numbers')
      mobile_ids = fields.One2many('project.mobilenumbers', 'partner_id', string='mobile numbers',required=True)
      order_ids =  fields.One2many('pos.order','delivery_man_id',select=True, string='Latest Orders', limit=5)
      status=fields.Selection([('a','Avaliable'),('b','Busy')],readonly=True)
      notes=fields.Html(string='Notes')
      address = fields.Char(string="Address")
      street= fields.Char(string='Street')
      city= fields.Char(string='City')
      state_id= fields.Many2one("res.country.state", string='State', ondelete='restrict')
      country_id= fields.Many2one('res.country', string='Country', ondelete='restrict')

      @api.multi
      def write(self, values):
          pattern = re.compile("^[0-9]{6,10}$")
          pattern1 = re.compile("^[0-9]{11}$")
          pattern2=re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
		            +"[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
          if 'mobile_ids' in values.keys():
              for mobile in values['mobile_ids']:
                if   mobile[2] != False:
                  if pattern1.match(mobile[2]['mobile_nu']):
                      pass
                  else:
                      raise exceptions.ValidationError("mobile numbers can only be integers must be  11 numbers")

          if 'phone_ids' in values.keys():
              for phone in values['phone_ids']:
                  if phone[2] != False :
                      if pattern.match(phone[2]['phone_nu']) :
                         pass
                      else:
                         raise exceptions.ValidationError("Phone  numbers can only be integers at least 6 numbers")

          if 'email' in values.keys():
                  if pattern2.match(values['email']):
                      pass
                  else:
                      raise exceptions.ValidationError("Not valid email address");


          if 'order_ids' in values.keys():
              for order in values['order_ids']:
                  order_record = self.env['pos.order'].search([('id', '=', order[1])])
                  if order_record['state'] == 'draft':
                     order_record['state'] =  'out'
          return super(delivery, self).write(values)

