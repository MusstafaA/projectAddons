{
    'name': 'POS Reports',
    'version': '1.0',
    'author': 'Mostafa Abd El Fattah',
    'category': 'other',
    'depends':['base','point_of_sale','hr'],
    'website': 'http://iti.gov.eg',
    'description':"""
All Point of sale reports which you can print
==========================
    """,# here we are importing all the views that we made before
    'data': [
        'pos_reports_view.xml',
     ],

}