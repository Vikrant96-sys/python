from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Vikrant!</h1>"

@app.route('/user/<name>')
def user(name):
	return '<h5>Hello, {0}!</h5>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)

