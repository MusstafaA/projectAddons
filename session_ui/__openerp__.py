{
    'name': 'POS Session Modifications',
    'version': '1.0',
    'author': 'OSAD_Odoo_Team',
    'category': 'other',
    'depends':['base','point_of_sale'],
    'website': 'http://iti.gov.eg',
    'description':"""
POS_Session_Modifications
==========================
    """,# here we are importing all the views that we made before
    'data': [
        'views/pos_dashboard_view.xml',
            ],
}