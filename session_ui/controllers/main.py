# -*- coding: utf-8 -*-
import logging
import werkzeug.utils

from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.web import http

# Print debug message
_logger = logging.getLogger(__name__)


class SessionController(http.Controller):

    @http.route('/pos/startup', type='http', auth='user',  website=True)
    def startup(self, debug=False, **k):
		return request.website.render("website.services",{'name':"Mostafa"})	
		#return "<h1>This is a test</h1>"


class PosController(http.Controller):

	@http.route('/pos/web', type='http', auth='user')
	def a(self, debug=False, **k):
		cr, uid, context, session = request.cr, request.uid, request.context, request.session

		# if user not logged in, log him in
		PosSession = request.registry['pos.session']
		pos_session_ids = PosSession.search(cr, uid, [('state','=','opened'),('user_id','=',session.uid)], context=context)
		if not pos_session_ids:
		    return werkzeug.utils.redirect('/web#action=point_of_sale.action_client_pos_menu')
		PosSession.login(cr, uid, pos_session_ids, context=context)

		return request.render('point_of_sale.index')		