{
    'name': 'Zulip Manipulator',
    'version': '0.0.1',
    'description': "Сreating tasks in odoo using a bot in Zulip",
    'website': 'https://nvt.miem.hse.ru',
    'author': '239',
    'depends': [
        'base',
        'project',
        'zulip_integration',
    ],
    'application': True,
    'data': [
        'views/zulip_channel_view.xml',
    ],
}
