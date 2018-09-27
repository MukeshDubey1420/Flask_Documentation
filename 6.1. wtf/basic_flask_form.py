from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myseckey'

class InfoForm(FlaskForm):

    username = StringField('Enter your User Name')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    un = ''
    form_1 = InfoForm()
    if form_1.validate_on_submit():
        un = form_1.username.data
    return render_template('home.html', form=form_1, user=un)


if __name__ == '__main__':
    app.run(debug=True)
