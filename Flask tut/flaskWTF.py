from flask_wtf import Form 
from wtforms import TextField , IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class Contact(Form):
	name= TextField('Name of Student',[validators.Required('Please fill the name field')])
	gen = RadioField('gender', choices = [('M','male'),('F','Female')])
	add = TextAreaField('address')
	email = TextField('e-mail',[validators.Required('please enter'),validators.Email('please enter valid email')])
	age = IntegerField('age')
	language = SelectField('lang', choices = [('Hindi','Guj'),('py','c')])
	sub= SubmitField('Send')
