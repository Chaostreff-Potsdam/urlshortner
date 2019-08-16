import urllib.parse

import wtforms
from wtforms import validators
from flask_wtf.recaptcha import RecaptchaField

from app import app, db
from url.models import Url

forbidden_routes = ["static", "admin", "stats", "api", "new", "preview", "p", "s"]

def supplyscheme(url, defaultscheme="https"):
    """ Prepends a scheme:// to url if no scheme provided """
    newurl = urllib.parse.urlparse(url, scheme=defaultscheme).geturl()
    # According to RFC1808 urllib.parse.urlparse makes a netloc to path
    # if no scheme is provided. This means we end up with tree slashes
    #    (scheme:///netloc-becoming-path)
    return newurl.replace(defaultscheme+":///", defaultscheme+"://")

class UrlForm(wtforms.Form):
    old = wtforms.StringField(label='', description='Enter full URL',  validators=[validators.DataRequired('If URL\'s were that short, would you even be here?')])
    new = wtforms.StringField(label=app.config["SERVER_NAME"]+"/", description='(optional) enter target')

    if app.config["RECAPTCHA_PUBLIC_KEY"]:
        recaptcha = RecaptchaField()

    def validate_new(form, field):
       new = field.data
       if '/' in new:
           raise validators.ValidationError("Links may not contain /")
       if db.session.query(db.exists().where(new == Url.new)).scalar() or (new in forbidden_routes):
           raise validators.ValidationError("URL already taken.")

    def save_url(self, url):
        self.populate_obj(url)
        url.old = supplyscheme(url.old)
        return url
