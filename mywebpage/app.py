from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

print("test")
class NameForm(FlaskForm):
    name = StringField('Which actor is your 1st favorite?', validators=[DataRequired()])
    name2 = StringField('Which actor is your 2st favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = '0<PI7yXq<U#n%IvXlqfI-RzD/:>5sdB/w)6si9MfyFzr[-"5h1~?)xdjh/&Y;'
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
 #   names = get_names(ACTORS)
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        # if name.lower() in names:
        #     # empty the form field
        #     form.name.data = ""
        #     id = get_id(ACTORS, name)
        #     # redirect the browser to another route and template
        #     return redirect( url_for('actor', id=id) )
        # else:
        #     message = "That actor is not in our database."
    return render_template('index.html', names=name, form=form, message=message)