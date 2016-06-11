from openerp import models, fields

class HrsEmployeeInherit(models.Model):
    #to link the model in the other Module Hr
    _inherit = 'hr.employee'