from wtforms import Form, StringField, TextField
from wtforms import HiddenField, IntegerField, BooleanField
from wtforms.validators import Required, Length, DataRequired

class FormVotacion(Form):
    id_persona = IntegerField(
                            'Id persona',
                            validators=[DataRequired(message = 'Id requerido')])
