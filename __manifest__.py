{
    'name': 'Cheque Management',
    'version': '1.0',
    'depends': ['base', 'report'],
    'data': [
        'views/cheque_views.xml',
        'report/cheque_report.xml',
        'report/cheque_report_action.xml',  # Rapor action'ının burada tanımlanması gerektiğini unutmayın
    ],
    'installable': True,
    'auto_install': False,
}
