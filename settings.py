import os

#######################################################################
###
###  Documentation of available options.
###  Use local_settings.py if you don't want to leak passwords etc.
###

APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '<Rk65mpq1nz8du0DLnSfLdQ>'


## Disable this in production environments

DEBUG = True


## Shows/Hides an usage list of all active links

ENABLE_STATS = False


## Adapt these to match your requirements
##    https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

SQLALCHEMY_DATABASE_URI = os.path.sep.join(["sqlite:///", APPLICATION_DIR, "test.sqlite"])


## Change to something else than None to enable captchas
## Get your own keys at https://www.google.com/recaptcha/admin
## When singing up select API-Version 2

RECAPTCHA_PUBLIC_KEY = None 
RECAPTCHA_PRIVATE_KEY = None
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}


## Where to bind to (testing context)

SERVER_NAME = 'localhost:5000'


## Change this to YourDomain.com in production

HOST_NAME = SERVER_NAME


## To overwrite any settings (without leaking confidental
## data to git) add and edit local_settings.py.

try:
    from local_settings import *
except ImportError:
    pass
