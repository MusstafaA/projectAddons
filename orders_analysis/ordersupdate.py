from openerp import models, fields, api


class OrdersUpdate(models.Model):
    _inherit = 'pos.order'
''''
    def _amount_line_tax(self, cr, uid, line, fiscal_position_id, context=None):
        # type: (object, object, object, object, object) -> object
        taxes = line.tax_ids.filtered(lambda t: t.company_id.id == line.order_id.company_id.id)
        if fiscal_position_id:
            taxes = fiscal_position_id.map_tax(taxes)
        price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
        cur = line.order_id.pricelist_id.currency_id
        taxes = \
        taxes.compute_all(price, cur, line.qty, product=line.product_id, partner=line.order_id.partner_id or False)[
            'taxes']
        val = 0.0
        for c in taxes:
            val += c.get('amount', 0.0)
        return val

    @api.multi
    def _amount_all(self):
        cr = self.env.cr
        uid = self.env.uid
        context=self.env.context
        cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self:
            res[order.id] = {
                'amount_paid': 0.0,
                'amount_return': 0.0,
                'amount_tax': 0.0,
            }
            val1 = val2 = 0.0
            cur = order.pricelist_id.currency_id
            for payment in order.statement_ids:
                res[order.id]['amount_paid'] += payment.amount
                res[order.id]['amount_return'] += (payment.amount < 0 and payment.amount or 0)
            for line in order.lines:
                val1 += self._amount_line_tax(cr, uid, line, order.fiscal_position_id,context)
                val2 += line.price_subtotal
            res[order.id]['amount_tax'] = cur_obj.round(cr, uid, cur, val1)
            amount_untaxed = cur_obj.round(cr, uid, cur, val2)
            res[order.id]['amount_total'] = res[order.id]['amount_tax'] + amount_untaxed
        return res
    amount_total = fields.Float(compute=_amount_all, string='Total', digits=0, multi='all', store=True)

    amount_tax = fields.Float(compute=_amount_all, string='Taxes', digits=0, multi='all')


    amount_paid = fields.Float(compute=_amount_all, string='Paid', states={'draft': [('readonly', False)]},
                               readonly=True, digits=0, multi='all')
    amount_return = fields.Float(compute=_amount_all, string='Returned', digits=0, multi='all')

 '''
'''
    @api.multi
    def _amount_all(self):
        cr=self._cr
        uid=self.env.uid
        ids=self.ids
        name=self.name_get
        args=None
        res = super(OrdersUpdate, self)._amount_all(cr, uid, ids,name,args,context=None)
        return res

    @api.multi
    def _amount_all(self):
        cr = self.env.cr
        uid = self.env.uid
        cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self:
            res[order.id] = {
                'amount_paid': 0.0,
                'amount_return': 0.0,
                'amount_tax': 0.0,
            }
            val1 = val2 = 0.0
            cur = order.pricelist_id.currency_id
            for payment in order.statement_ids:
                res[order.id]['amount_paid'] += payment.amount
                res[order.id]['amount_return'] += (payment.amount < 0 and payment.amount or 0)
            for line in order.lines:
                val1 += self._amount_line_tax(cr, uid, line, order.fiscal_position_id, context=None)
                val2 += line.price_subtotal
            res[order.id]['amount_tax'] = cur_obj.round(cr, uid, cur, val1)
            amount_untaxed = cur_obj.round(cr, uid, cur, val2)
            res[order.id]['amount_total'] = res[order.id]['amount_tax'] + amount_untaxed
        return res

    amount_tax = fields.Float(compute=_amount_all, string='Taxes', digits=0, multi='all')


            amount_paid = fields.Float(compute=_amount_all, string='Paid', states={'draft': [('readonly', False)]},
                               readonly=True, digits=0, multi='all')
    amount_return = fields.Float(compute=_amount_all, string='Returned', digits=0, multi='all')

'''