from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, length



class ContactForm(FlaskForm):
    name = StringField('Full Name:')
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    message = TextAreaField('Message:', validators=[DataRequired(), length(max=500)])
    submit = SubmitField('Contact')
