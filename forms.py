from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField
from wtforms.validators import InputRequired, Length


class ArticleForm(FlaskForm):
    user = StringField('User', validators=[InputRequired(), Length(max=25)])
    title = StringField('Title', validators=[InputRequired(), Length(max=1000)])
    article = TextAreaField('Text', validators=[InputRequired(), Length(max=200000)])

class EditArticleForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=1000)])
    article = TextAreaField('Text', validators=[InputRequired(), Length(max=200000)])