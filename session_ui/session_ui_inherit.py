from openerp import models, fields


class PosConfigInherit(models.Model):
    #to link the model in the other Module Hr
	_inherit = 'pos.config'
	emp_code = fields.Char()
    # Methods to open the POS
	def open_start_up(self, cr, uid, ids, context=None):
		assert len(ids) == 1, "you can open only one session at a time"

		record = self.browse(cr, uid, ids[0], context=context)
		context = dict(context or {})
		context['active_id'] = record.current_session_id.id
		return {
			'type': 'ir.actions.act_url',
			'url':   '/pos/startup',
			'target': 'self',
				}

	# Methods to open the POS

	def open_ui_in(self, cr, uid, ids, context=None):
		assert len(ids) == 1, "you can open only one session at a time"

		record = self.browse(cr, uid, ids[0], context=context)
		context = dict(context or {})
		context['active_id'] = record.current_session_id.id
		return {
			'type': 'ir.actions.act_url',
			'url':   '/pos/startup',
			'target': 'self',
				}
