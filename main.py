from flask import Flask, render_template
from app1.app1 import app1
from app2.app2 import app2
from app3.app3 import app3

app = Flask(__name__)

app.register_blueprint(app1, url_prefix='/app1')
app.register_blueprint(app2, url_prefix='/app2')
app.register_blueprint(app3, url_prefix='/app3')

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
