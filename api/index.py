# -*- coding:utf-8 -*-

from core.appConfig import appConfig
from core.helpers.timeStamp import getTimeStamp
from core.logger import getLogger
from flaskApp.flaskApp import flaskApp

from sample.sampleRoutes import sampleRoutes

#  from sample.sampleApp import sampleApp

LOCAL = appConfig.get('LOCAL')
WERKZEUG_RUN_MAIN = appConfig.get('WERKZEUG_RUN_MAIN')

logger = getLogger('api/index')

logger.info('App started, LOCAL=%s, WERKZEUG_RUN_MAIN=%s' % (LOCAL, WERKZEUG_RUN_MAIN))

# TODO: Ensure initializing only once (avoiding double initialization with `* Restarting with stat`...)
#  isMain = WERKZEUG_RUN_MAIN == 'true'
#  doInit = True  # not LOCAL or isMain

# Initalize all the routes...
flaskApp.register_blueprint(sampleRoutes, url_prefix='/')

# Expose `app` variable...
app = flaskApp
__all__ = ['app']


if __name__ == '__main__':
    logger.debug('LOCAL: %s' % LOCAL)
