from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Elevatorpitch','Elevatorpitch'), ('Pickuplines','Pickuplines'), ('Puns','Puns')],validators=[DataRequired()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')