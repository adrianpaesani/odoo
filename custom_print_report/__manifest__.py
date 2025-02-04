# -*- coding: utf-8 -*-
##############################################################################
#
#    Haresh Kansara
#    Copyright (C) 2020-TODAY Haresh Kansara(hareshkansara00@gmail.com).
#    Author: Haresh Kansara(hareshkansara00@gmail.com).
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Custom Print Report",
    "version": "13.0.0.1",
    "category": "Sales",
    "license": "AGPL-3",
    'author': 'Haresh Kansara',
    'maintainer': 'Haresh Kansara',
    'website': 'hareshkansara.odoo.com',
    'support': 'hareshkansara00@gmail.com',
    'summary': 'Custom Print Report For Sales/Quotation and Invoices',
    'description': 'Custom Print Report For Sales/Quotation and Invoices',
    "depends": [
        'sale_quotation_builder',
        'payment',
        'sale_management',
        'helpdesk',
        'contacts',
        'website_sale_delivery',
        'auth_signup',
        'sale_stock',
        'website_sale',
    ],
    "data": [
        'security/security.xml',
        'data/data.xml',
        'views/assets.xml',
        'views/sale_quote_template_view.xml',
        'views/stock_picking_view.xml',
        # Templates
        'templates/sale_template.xml',
        'templates/auth_signup_template.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
}
