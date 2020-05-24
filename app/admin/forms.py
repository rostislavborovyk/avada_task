from flask_wtf import FlaskForm
from wtforms import FileField


class TopBannerForm(FlaskForm):
    file = FileField()



