from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/<age>/<hn>/<ha>/<sn>')
def user(name,age,hn,ha,sn):
    return render_template('user.html', name=name, age=age, hn=hn, ha=ha, sn=sn)

if __name__ == '__main__':
    app.run(debug=True)

