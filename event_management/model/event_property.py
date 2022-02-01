from odoo import models, fields


class EventType(models.Model):
    _name = "event.property"
    _description = " Event Type "
    name = fields.Char()
    code = fields.Integer()
    image = fields.Image()


