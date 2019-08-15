import wtforms
from wtforms import validators
from flask_wtf.recaptcha import RecaptchaField

from app import app, db
from url.models import Url

forbidden_routes = ["static", "admin", "stats", "api", "new", "preview", "p"]

class UrlForm(wtforms.Form):
    old = wtforms.StringField(label='', description='Enter full URL',  validators=[validators.DataRequired('If URL\'s were that short, would you even be here?')])
    new = wtforms.StringField(label=app.config["HOST_NAME"]+"/", description='(optional) enter target')

    if app.config["RECAPTCHA_PUBLIC_KEY"]:
        recaptcha = RecaptchaField()

    def validate_new(form, field):
       new = field.data
       if '/' in new:
           raise validators.ValidationError("Contains invalid characters")
       if db.session.query(db.exists().where(new == Url.new)).scalar() or (new in forbidden_routes):
           raise validators.ValidationError("URL already taken.")

    def save_url(self, url):
        self.populate_obj(url)
        if not "http" in url.old:
            url.old = "http://" + url.old
        return url
