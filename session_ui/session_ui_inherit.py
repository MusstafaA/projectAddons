from openerp import models, fields

class PosConfigInherit(models.Model):
    #to link the model in the other Module Hr
    _inherit = 'pos.config'
    emp_code = fields.Char()