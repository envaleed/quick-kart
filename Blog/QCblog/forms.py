from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from QCblog.models import User

class RegistrationForm(FlaskForm):
	username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired()])
	confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit= SubmitField('Sign up')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Sorry that name is taken.')
	
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email is already in use.')
	
class LoginForm(FlaskForm):
	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired()])
	remember= BooleanField('Remember Me')
	submit= SubmitField('Login')
	
class RecipeForm(FlaskForm):
	title= StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
	recipe= TextAreaField('Recipe', validators=[DataRequired()])
	submit= SubmitField('Add Recipe')

class PostForm(FlaskForm):
	title= StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
	post= TextAreaField('Post', validators=[DataRequired()])
	submit= SubmitField('Create Post')
