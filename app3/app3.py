from flask import Blueprint, render_template

app3 = Blueprint('app3', __name__,
                 static_folder='static',
                 template_folder='templates')

@app3.route('/home')
@app3.route('/')
def home():
    return render_template('app3.html')
