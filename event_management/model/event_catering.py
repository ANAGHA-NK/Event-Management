from pyasn1_modules.rfc2985 import SequenceNumber
from odoo import models, fields, api
from odoo.fields import Selection


class EventCatering(models.Model):
    _name = "event.catering"
    _description = " Event Catering "

    sequence = fields.Char(string="Sequence Number", readonly=True, copy=False)
    event = fields.Char()
    date = fields.Date()
    start_date = fields.Date()
    end_date = fields.Date()
    guests = fields.Integer()
    welcome_drink = fields.Boolean()
    breakfast = fields.Boolean()
    lunch = fields.Boolean()
    dinner = fields.Boolean()
    snacks_and_drinks = fields.Boolean()
    beverages = fields.Boolean()
    notebook_ids = fields.One2many('event.ord', 'items')
    name = fields.Char()
    uom = fields.Char()
    state: Selection = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                                         ('delivered', 'Delivered'), ('invoiced', 'Invoiced'),
                                         ('expired', 'Expired'), ],
                                        required=True,
                                        default='draft')

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New'
        sequence = super(EventCatering, self).create(vals)
        return sequence



# menu

# class EventOrder(models.Model):
#     _name = "event.order"
#     _description = " Event Service "
#     notebook_ids = fields.One2many('event.ord', 'ord_id')
#     name = fields.Char()
# respondsible_person = fields.Char()

#
class EventOrd(models.Model):
    _name = 'event.ord'
    items = fields.Many2one('event.catmenu', string="Items")
    # items = fields.Char()
    description = fields.Text()
    quantity = fields.Integer()
    uom = fields.Char()
    unit_price = fields.Integer()
    # sub_total = fields.Integer()
    line_sub_total = fields.Float(string='sub total', compute='_compute_sub_total')

    def _compute_sub_total(self):
        for line in self:
            line_sub_total = 0
            if line.quantity and line.unit_price:
                line_sub_total += (line.quantity * line.unit_price)
                line.line_sub_total = line_sub_total
