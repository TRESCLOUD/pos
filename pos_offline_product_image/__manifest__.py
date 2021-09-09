# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS offline product image',
    'version': '1.0',
    'category': 'Point Of Sale',
    'summary': 'Load product images at POS start and shows base64 image instead of image url',
    'author': 'TRESCLOUD CIA LTDA',
    'maintainer': 'TRESCLOUD CIA. LTDA.',
    'website': 'http://www.trescloud.com',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/js_load_files.xml',
    ],
    'qweb': [],
    'installable': True,
}
