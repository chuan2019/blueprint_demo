from flask import Blueprint, render_template

app2 = Blueprint('app2', __name__,
                 static_folder='static',
                 template_folder='templates')

@app2.route('/home')
@app2.route('/')
def home():
    return render_template('app2.html')
