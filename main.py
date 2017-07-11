from flask import Flask, render_template, redirect, url_for, session
from dummy_script import print_to_console, return_rand_int

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/')
def landing():
	return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
	rand_int = session.get('rand_int', None)
	return render_template('dashboard.html', rand_int=rand_int)

@app.route('/execute-script')
def executeScript():
	session['rand_int'] = return_rand_int()
	print_to_console()

	return redirect(url_for('dashboard'))

if __name__ == "__main__":
	app.run()