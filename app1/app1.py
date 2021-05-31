from flask import Blueprint, render_template

app1 = Blueprint('app1', __name__,
                 static_folder='static',
                 template_folder='templates')

@app1.route('/home')
@app1.route('/')
def home():
    return render_template('app1.html')
