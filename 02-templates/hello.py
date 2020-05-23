from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/<age>')
def user(name,age):
    return render_template('user.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)

