# -*- coding: utf-8 -*-
{
    'name': "Reporte de facturas personalizado",
    'summary': """
        Personalización de reporte de facturas
    """,
    'description': """
        Personalización de reporte de facturas con un formato diferente al usado por odoo.
    """,
    'author': "M22",
    'website': "https://m22.mx",
    'category': 'Contabilidad',
    'version': '16.0.1',
    'depends': ['base','stock_account','account','l10n_mx_edi','l10n_mx_edi_40'],
    'data': [
        'reports/report_invoice_document.xml'
    ],
    'license': 'AGPL-3'
}
