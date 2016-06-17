# coding=utf-8
import re
from openerp import models, fields, api, exceptions
from datetime import datetime

from openerp.osv import osv


class OrderUpdate(models.Model):
    _inherit = 'pos.order'
    state = fields.Selection([('draft', 'New'),
                              ('out', 'Out for delivery'),
                              ('cancel', 'Cancelled'),
                              ('paid', 'Paid'),
                              ('done', 'Posted'),
                              ('invoiced', 'Invoiced')],
                             'Status', readonly=True)
    manuf_time = fields.Char(compute='compute_manufacturing_time', string="Manufacturing")
    delivery_time = fields.Char(compute='compute_delivery_time', string="Delivery")
    out_for_delivery_at = fields.Datetime()
    shipping_cost = fields.Float(compute='compute_shipping_cost', string='Shipping Cost')
    total_amount =fields.Float(compute='compute_total')


    @api.multi
    def compute_manufacturing_time(self):
        fmt = '%Y-%m-%d %H:%M:%S'
        now = datetime.now()
        current_datetime = str(now)[:19]
        for record in self:
            if record.state == 'draft':
                date_from = datetime.strptime(current_datetime, fmt)
                date_to = datetime.strptime(record.create_date, fmt)
                difference = date_from - date_to

                minutes, seconds = divmod(difference.seconds + difference.days * 86400, 60)
                hours, minutes = divmod(minutes, 60)
                record.manuf_time = '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

    @api.multi
    def compute_delivery_time(self):
        fmt = '%Y-%m-%d %H:%M:%S'
        now = datetime.now()
        current_datetime = str(now)[:19]
        for record in self:
            if record.state == 'out':
                date_from = datetime.strptime(current_datetime, fmt)
                date_to = datetime.strptime(record.out_for_delivery_at, fmt)
                difference = date_from - date_to

                minutes, seconds = divmod(difference.seconds + difference.days * 86400, 60)
                hours, minutes = divmod(minutes, 60)
                record.delivery_time = '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

    @api.multi
    def compute_shipping_cost(self):
        for record in self:
            if record.zone == 'A':
               record.shipping_cost = 10.01
            elif record.zone == 'B':
                record.shipping_cost = 20.01
            elif record.zone == 'B':
                record.shipping_cost = 30.01
            elif record.zone == 'B':
                record.shipping_cost = 40.1
            else:
                record.shipping_cost = 50.1



    @api.multi
    def compute_total(self):
        for record in self:
            a = self.env['pos.order'].browse([record.id])._amount_all(self._cr, self._uid)
            record.total_amount = a[record.id]['amount_total'] + record.shipping_cost
            #record.amount_total = a[record.id]['amount_total'] + 42

            # @api.multi
            # def compute_manuf(self):
            # for record in self:
            # joining_date = record.create_date
            # current_date = (datetime.today()).strftime(fmt)

            # d1 = datetime.strptime(joining_date, fmt).time()
            # d2 = datetime.strptime(current_date, fmt).time()
            # r = relativedelta(d2,d1)
            # record.total_hours= int(d2_ts-d1_ts) / 60


class delivery(models.Model):
    _inherit = 'project.delivery'

    @api.multi
    def write(self, values):
        if 'order_ids' in values.keys():
            now = datetime.now()
            current_datetime = str(now)[:19]
            for order in values['order_ids']:
                order_record = self.env['pos.order'].search([('id', '=', order[1])])
                if order_record['state'] == 'draft':
                    order_record['out_for_delivery_at'] = current_datetime
        return super(delivery, self).write(values)


class pos_orders(models.Model):
    _inherit = 'pos.order'

    # def _amount_all(self):
    #     res = super(pos_orders, self)._amount_all(self._cr, self._uid)
    #     for order in self.browse():
    #         res[order.id]['amount_total'] += order.shipping_cost
    #         order.totals = res[order.id]['amount_total']
    #     return res

    # amount_tax = fields.Float(compute='_amount_all', string='Taxes')
    # amount_total = fields.Float(compute='_amount_all', string='Total')

