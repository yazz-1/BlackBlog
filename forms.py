from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class ArticleForm(FlaskForm):
    user = StringField('User', validators=[InputRequired(), Length(min=4), Length(max=25)])
    title = StringField('Title', validators=[InputRequired(), Length(max=1000)])
    article = TextAreaField('Text', validators=[InputRequired(), Length(max=200000)])

class EditArticleForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=1000)])
    article = TextAreaField('Text', validators=[InputRequired(), Length(max=200000)])

class RegisterForm(FlaskForm):
    user = StringField('Username', validators=[InputRequired(), Length(min=4), Length(max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    email = StringField('Valid Email Adress', validators=[InputRequired(), Email()])

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[InputRequired(), Length(min=4), Length(max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])