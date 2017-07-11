from flask import Flask, render_template, redirect, url_for, session
from dummy_script import print_to_console, return_rand_int
import requests

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/')
def landing():
	return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
	rand_int = session.get('rand_int', None)
	get_req = session.get('get_req', None)

	return render_template('dashboard.html', rand_int=rand_int, get_req=get_req)

@app.route('/random-int')
def randomInt():
	session['rand_int'] = return_rand_int()
	print_to_console()

	return redirect(url_for('dashboard'))

@app.route('/web-api')
def webAPI():
	session['get_req'] = (requests.get('https://jsonplaceholder.typicode.com/posts/' + str(return_rand_int()))).text

	return redirect(url_for('dashboard'))

if __name__ == "__main__":
	app.run()