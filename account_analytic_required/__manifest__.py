##############################################################################
#
#    Desarrollado por Quilsoft para la
#    Direccion General de Rentas Provincia de Misiones Republica Argentina
#    quien ostenta los derechos de Copyright
#    2022 All Rights Reserved.
#
##############################################################################

{
    'name': 'Account Analytic Required',
    'version': '14.0.0.1',
    'category': 'account',
    'summary': '',
    'author': "Quilsoft",
    'license': 'AGPL-3',
    'depends': [
        'account','account_tax_settlement'
    ],
    'data': [
        'views/account_account.xml',
        'views/account_journal_view.xml',
        #'security/rules.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
