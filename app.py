from flask import Flask, redirect,url_for

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():  # put application's code here
    return 'welcome to home page'

@app.route('/cakes')
def cakes_func():
    return 'Hello to cakes page!'

@app.route('/about')
def about_func():
    # todo
    # do something with db
    print('i am in about')
    return redirect('/cakes')

@app.route('/cart')
def cart_func():
    # todo
    # do something with db
    print('you are at our shopping cart page')
    return redirect(url_for('cakes_func'))


if __name__ == '_main_':
    app.run(debug=True)