from openerp import models ,fields , api 

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
      name = fields.Char()
      email=fields.Char()
      image = fields.Binary()
      date_of_birth = fields.Date()
      phone_ids =  fields.One2many('project.phonenumbers', 'partner_id', string='phone numbers')
      mobile_ids = fields.One2many('project.mobilenumbers', 'partner_id', string='mobile numbers')
      order_ids =  fields.One2many('pos.order','delivery_man_id',select=True, string='Latest Orders', limit=5)
      status=fields.Selection([('a','Avaliable'),('b','Busy')],readonly=True)
      notes=fields.Html(string='Notes')        