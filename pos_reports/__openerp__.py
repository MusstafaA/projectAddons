{
    'name': 'POS Reports',
    'version': '1.0',
    'author': 'Mostafa Abd El Fattah',
    'category': 'other',
    'depends':['base','point_of_sale','report','web'],
    'website': 'http://iti.gov.eg',
    'description':"""
All Point of sale reports which you can print
==========================
    """,# here we are importing all the views that we made before
    'data': [
        'data/report_paperformat.xml',
        'pos_reports_view.xml',
        'views/order_customer_details.xml',
        'views/products_to_customer.xml',
        'pos_reports_template.xml',
         ],

}