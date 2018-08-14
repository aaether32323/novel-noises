from flask import Flask, render_template

app = Flask(__name__)
# app.config.from_pyfile('config.py')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')