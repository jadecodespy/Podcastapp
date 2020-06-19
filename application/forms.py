from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from application import db


class UpdateTopicsForm(FlaskForm):
     title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    
     )
     
     
     description = StringField('Description',
             validators = [
                 DataRequired(),
                 Length(min=4,max=250)
             ]
     )
    
     submit = SubmitField('Update')






class Addtopics(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=100)

            ]
    )



    description = StringField('Description',
            validators = [
                DataRequired(),
                Length(min=4,max=250)

            ]
    )


    submit = SubmitField('Add Topic')


class Addpodcast(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=100)

            ]
    )



    detail = StringField('Podcast Detail',
            validators = [
                DataRequired(),
                Length(min=4,max=250)

            ]
    )

    topic_one = StringField('Topic title',
            validators = [
                Length(max = 100)
            ]

    )

    submit = SubmitField('Add a Podcast')





