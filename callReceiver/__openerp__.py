{
    'name' : 'Delivery Call Receiver',
    'version' : '1.0',
    'author': 'Pos Team',
    'category': 'other',
    'website': 'http://iti.gov.eg',
    'depends': ['point_of_sale'],
    'description': """
Testing
======
    """,
    'data': [
                'receiver_view.xml',
                'views/call_receiver_templ.xml',
                'delivery_table_view.xml',


             ],
    'js': ['static/src/js/widgets.js'],
    'qweb': [
                'static/src/xml/pos.xml',
                # 'static/src/xml/widgets.xml'

             ],

}
