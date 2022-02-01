from odoo import models, fields


class EventService(models.Model):
    _name = "event.security"
    _description = " Event Service "
    notebook_ids = fields.One2many('event.services', 'service_id')
    name = fields.Char()
    respondsible_person = fields.Char()


class ServiceMod(models.Model):
    _name = 'event.services'
    service_id = fields.Many2one('event.security')
    description = fields.Text()
    quantity = fields.Integer()
    unit_price = fields.Integer()
    # sub_total = fields.Integer()
    line_sub_total = fields.Float(string='sub total', compute='_compute_sub_total')

    def _compute_sub_total(self):
        for line in self:
            line_sub_total = 0
            if line.quantity and line.unit_price:
                line_sub_total += (line.quantity * line.unit_price)
                line.line_sub_total = line_sub_total
