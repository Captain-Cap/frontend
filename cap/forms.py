from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddBalloonForm(FlaskForm):
    firm = StringField('Firm', validators=[DataRequired()], render_kw={'class': 'form-control'})
    paint_code = StringField('Paint code', validators=[DataRequired()], render_kw={'class': 'form-control'})
    color = StringField('Color', validators=[DataRequired()], render_kw={'class': 'form-control'})
    volume = IntegerField('Volume', validators=[DataRequired()], render_kw={'class': 'form-control'})
    weight = IntegerField('Weight', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-dark'})
