from flask_wtf import FlaskForm , RecaptchaField

class loginuse(FlaskForm):
    rec = RecaptchaField()