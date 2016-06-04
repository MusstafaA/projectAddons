from openerp import models ,fields , api , api ,exceptions
import re

class PhoneNumbers(models.Model):
        _name='project.phonenumbers'
        phone_nu=fields.Char(string='Phone numbers')
        partner_id = fields.Many2one('res.partner')


class MobileNumbers(models.Model):
        _name = 'project.mobilenumbers'
        mobile_nu = fields.Char(string='Mobile numbers')
        partner_id=fields.Many2one('res.partner')

class OrderUpdate(models.Model):
        _inherit='pos.order'
        delivery_man_id=fields.Many2one('project.delivery')

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

        @api.multi
      def write(self, values):
          values;
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
                  if pattern.match(values['email']):
                      pass
                  else:
                      raise exceptions.ValidationError("Not valid email");    