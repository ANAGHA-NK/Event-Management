from odoo import models, fields


class EventCatMenu(models.Model):
    _name = "event.catmenu"
    _description = " Event Catering Menu"
    name = fields.Char()
    category = fields.Selection(
        selection=[('welcome_drink', 'Welcome Drink'), ('break_fast', 'Break Fast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snacks_and_drinks', ' Snacks and Drinks'), ('beverages', 'Beverages')])
    image = fields.Image()
    uom = fields.Char()
    unit_price = fields.Integer()
    # notebook_ids = fields.One2many('event.catering')

