#!/bin/sh

CERT_PATH="/etc/letsencrypt/live/django-lms.duckdns.org/fullchain.pem"
CONF_PATH="/etc/nginx/conf.d/https.conf"
TEMPLATE_PATH="/etc/nginx/templates/https.conf"

if [ -f "$CERT_PATH" ]; then
    echo "✅ Сертифікат знайдено. Увімкнено HTTPS."
    cp "$TEMPLATE_PATH" "$CONF_PATH"
else
    echo "⚠️ Сертифікат не знайдено. Працює тільки HTTP."
    touch "$CONF_PATH"
fi

nginx -g "daemon off;"
