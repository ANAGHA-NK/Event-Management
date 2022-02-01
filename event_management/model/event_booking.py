from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class EventBooking(models.Model):
    _name = "event.booking"
    _inherit = ['mail.thread']
    _description = " Event Booking "
    name = fields.Char(track_visibilty='always')
    event_type_id = fields.Many2one('event.booking')
    customer = fields.Many2one('res.partner')
    # address = fields.Char()
    booking_date = fields.Datetime()
    start_date_and_time = fields.Date(string='Start Date')
    end_date_and_time = fields.Date(string='End Date')
    duration = fields.Integer(string='Duration', store=True, compute='_compute_duration')

    @api.onchange('start_date_and_time', 'end_date_and_time', 'duration')
    def _compute_duration(self):
        if self.start_date_and_time and self.end_date_and_time:
            d1 = datetime.strptime(str(self.start_date_and_time), '%Y-%m-%d')
            d2 = datetime.strptime(str(self.end_date_and_time), '%Y-%m-%d')
            d3 = d2 - d1
            self.duration = str(d3.days)


    # def my_button(self):
    #     return {
    #         event_type_id = fields.Many2one('event.booking')
    #     customer = fields.Many2one('res.partner')
    #     # address = fields.Char()
    #     booking_date = fields.Datetime()
    #     start_date_and_time = fields.Date(string='Start Date')
    #     end_date_and_time = fields.Date(string='End Date')
    #     }
