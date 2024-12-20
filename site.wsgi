import os, sys
activate_this = '/home/innfes/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/innfes/domains/smartwells.ru/market_django'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'market_django.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()