import time
from openerp.report import report_sxw
from openerp.osv import osv
from openerp import api, models

class pos_customer_products(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(pos_customer_products, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_products': self._get_products,
        })

    def _get_products(self, field):
        # lines=[]
        # for obj in objects:
        #     if user.id==obj.user_id.id:
        #         lines.append(obj)
        print self
        # return lines
        return "hello world!"

class report_pos_customer_products(osv.AbstractModel):
    _name = 'report.pos_reports.products_to_customer'
    _inherit = 'report.abstract_report'
    _template = 'pos_reports.products_to_customer'
    _wrapped_report_class = pos_customer_products        