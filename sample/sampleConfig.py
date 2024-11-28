# -*- coding:utf-8 -*-

from core.appConfig import appConfig

TELEGRAM_TOKEN = appConfig.get('TELEGRAM_TOKEN')  # Telegram token from env or vercel settings

VERCEL_URL = appConfig.get('VERCEL_URL', '')  # Should be provided by vercel environment for production

# TODO: Detect local ip, set WEBHOOK_URL to this ip as default
# print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
# Set env variable to get webhook host?

WEBHOOK_PREFIX = appConfig.get('WEBHOOK_PREFIX', 'https://')
WEBHOOK_HOST = appConfig.get('WEBHOOK_HOST', '127.0.0.1')  # Should be an ngrok relay link (for the local mode)
WEBHOOK_PATH = appConfig.get('WEBHOOK_PATH', '/webhook')  # Local route, see implementation in `botBlueprint.py`

# Compose correct webhook fully-qualified url...
WEBHOOK_RESOLVED_HOST = VERCEL_URL if VERCEL_URL else WEBHOOK_HOST
WEBHOOK_URL = WEBHOOK_RESOLVED_HOST + WEBHOOK_PATH
if not WEBHOOK_URL.startswith('http'):
    WEBHOOK_URL = WEBHOOK_PREFIX + WEBHOOK_URL
