from openerp import models ,fields , api 

class PhoneNumbers(models.Model):
        _name='project.phonenumbers'
        phone_nu=fields.Char(string='Phone numbers')
        partner_id = fields.Many2one('res.partner')


class MobileNumbers(models.Model):
        _name = 'project.mobilenumbers'
        mobile_nu = fields.Char(string='Mobile numbers')
        partner_id=fields.Many2one('res.partner')
