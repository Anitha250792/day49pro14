from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

class TicketForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    category = SelectField('Issue Category', choices=[
        ('billing', 'Billing'),
        ('technical', 'Technical'),
        ('account', 'Account'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Issue Description', validators=[DataRequired(), Length(min=25)])
    submit = SubmitField('Submit Ticket')
