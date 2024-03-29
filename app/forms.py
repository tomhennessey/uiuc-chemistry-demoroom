from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField, EmailField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    demo = StringField('Demo Name', validators=[DataRequired()])
    date_request = DateTimeLocalField('Date and Time of Demo', format='%Y-%m-%dT%H:%M')
    comments = TextAreaField('Additional Comments')
    submit = SubmitField('Request Demo')

class SearchForm(FlaskForm):
    name = StringField('Search for a demo:', validators=[DataRequired()])

