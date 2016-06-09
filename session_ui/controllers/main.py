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