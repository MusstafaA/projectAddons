{
    'name': 'POS Customer Modifications',
    'version': '1.0',
    'author': 'OSAD',
    'category': 'other',
    'depends':['base','point_of_sale'],
    'website': 'http://iti.gov.eg',
    'description':"""
POS_Customer_Modifications
==========================
    """,# here we are importing all the views that we made before
    'data': [
        'customer_modification_view.xml',
        'views/customer.xml',
        'views/customer_template.xml',
    ],

    'qweb': [
                'static/src/xml/pos.xml',
            ],
}