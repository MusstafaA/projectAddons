# -*- coding: utf-8 -*-
import logging
import werkzeug.utils

from openerp import http
from openerp.http import request

# Print debug message
_logger = logging.getLogger(__name__)


class SessionController(http.Controller):

    @http.route('/pos/startup', type='http', auth='user')
    def startup(self, debug=False, **k):
        return "<h1>This is a test</h1>"    

