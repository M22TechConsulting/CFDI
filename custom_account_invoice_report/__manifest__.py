# -*- coding: utf-8 -*-
{
    'name': "Reporte de facturas personalizado",
    'summary': """
        Personalización de reporte de facturas.
    """,
    'description': """
        Personalización de reporte de facturas con un formato diferente al usado por odoo.
    """,
    'author': "M22",
    'website': "https://m22.mx",
    'category': 'Contabilidad',
    'version': '16.0.1',
    'depends': ['base', 'sale', 'stock_account','l10n_mx_edi','l10n_mx_edi_40'],
    'data': [
        'reports/report_header_document.xml',
        'reports/report_invoice_document.xml',
        'reports/report_saleorder_pro_forma.xml',
        'reports/report_payment_receipt_document.xml'
    ],
    'assets': {
        'web.report_assets_common': [
            'custom_account_invoice_report/static/src/scss/style.scss',
        ],
    },
    'license': 'AGPL-3'
}
