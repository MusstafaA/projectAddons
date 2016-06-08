import re
from openerp import models, fields, api, exceptions
from datetime import datetime


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
