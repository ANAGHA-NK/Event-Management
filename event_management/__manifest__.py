
{
      'name': 'event',
      'depends': ['base', 'mail'],
      'application': True,
      'data': [
          'security/ir.model.access.csv',
          'views/event_property_views.xml',
          'views/event_booking_views.xml',
          'views/event_security_views.xml',
          'views/event_catering_view.xml',
          'views/event_catmenu_views.xml',
          'data/sequence.xml',
          'data/event_types.xml',
          'data/event_service_type.xml',
          'views/event_menus.xml',
      ]

}
