# -*- coding:utf-8 -*-

import time
import traceback
from flask import Blueprint
from flask import Response
from flask import request
#  import telebot # pyTelegramBotAPI

from core.helpers import errorToString
from core.helpers.timeStamp import getTimeStamp
from core.logger import getLogger
from core.appConfig import appConfig

from core.helpers import debugObj
from core.helpers.generic import dictFromModule

#  from bot.botApp import botApp
#  from .commands import registerCommands

from . import sampleConfig

startTimeStr = getTimeStamp(True)

logger = getLogger('sample/sampleRoutes')

# Flask blueprint routes to export
sampleRoutes = Blueprint('sampleRoutes', __name__)

logTraceback = False


# Trace keys in logger and reponses
debugKeysList = [
    'startTimeStr',
    'timeStr',
    'LOCAL',
    'WEBHOOK_URL',
]


def logSampleStarted():
    """
    Debug: Show application start info.
    """
    timeStr = getTimeStamp(True)
    obj = {
        **appConfig,
        **dictFromModule(sampleConfig),
        **{
            'startTimeStr': startTimeStr,
            'timeStr': timeStr,
        },
    }
    content = '\n\n'.join(
        [
            'logSampleStarted: sampleRoutes started',
            debugObj(obj, debugKeysList),
        ]
    )
    logger.info(content)


@sampleRoutes.route('/test')
def testRoute():
    timeStr = getTimeStamp(True)
    obj = {
        **appConfig,
        **dictFromModule(sampleConfig),
        **{
            'startTimeStr': startTimeStr,
            'timeStr': timeStr,
        },
    }
    content = '\n\n'.join(
        [
            'testRoute @ %s' % timeStr,
            debugObj(obj, debugKeysList),
        ]
    )
    logger.info(content)
    return Response(content, headers={'Content-type': 'text/plain'})


@sampleRoutes.route('/')
def sampleRoot():
    """
    Root page
    """
    timeStr = getTimeStamp(True)

    result: bool
    try:
        # TODO
        result = True # initWebhook()
    except Exception as err:
        sError = errorToString(err, show_stacktrace=False)
        sTraceback = str(traceback.format_exc())
        errMsg = 'sampleRoot: Error registering webhook: ' + sError
        if logTraceback:
            errMsg += sTraceback
        else:
            logger.info('sampleRoot: Traceback for the following error:' + sTraceback)
        logger.error(errMsg)
        return Response(errMsg, headers={'Content-type': 'text/plain'})

    obj = {
        **appConfig,
        **dictFromModule(sampleConfig),
        **{
            'startTimeStr': startTimeStr,
            'timeStr': timeStr,
        },
    }
    debugData = debugObj(obj, debugKeysList)
    content = '\n\n'.join(
        [
            'Sample root route',
            debugData,
        ]
    )
    logger.info(content)
    return Response(content, headers={'Content-type': 'text/plain'})

# DEBUG
logSampleStarted()

# TODO: Do other initialization stuff (like registering commands etc)

# Module exports...
__all__ = [
    'sampleRoutes',
]
