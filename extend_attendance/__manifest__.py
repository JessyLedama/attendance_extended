# -*- coding: utf-8 -*-
{
    'name': 'Attendance Extended',
    'category': 'HR/Attendance',
    'author': 'SIMI Technologies',
    'summary': 'Extend attendance module',
    'version': '0.9.1',
    'license': "LGPL-3",
    'sequence': 7,
    'description': """Extend Attendance""",

    'depends': ['hr.attendance',],
    'data': [
        'views/pos_payment_method_views.xml',
        'views/point_of_sale_assets.xml',
        'views/res_config_settings_views.xml',
        'views/ipay_pos_config.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'views/ipay_pos_demo.xml',
    ],
    'qweb': [
        'static/src/xml/ipay_pos_view_form.xml',
        'static/src/xml/ipay_order_receipt.xml'
    ],
    "images": ['static/description/ipay_cover.jpg'],
    'installable': True,
}
