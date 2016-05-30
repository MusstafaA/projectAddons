#this is the model inhertience

from openerp import models, fields

class HrEmployeeInherit(models.Model):
    #to link the model in the other Module Hr
    _inherit = 'hr.employee'
    emp_code = fields.Char()

