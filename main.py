from flask import Flask, render_template, redirect, url_for
from dummy_script import print_to_console

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/')
def landing():
	return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/execute-script')
def executeScript():
	print_to_console()

	return redirect(url_for('dashboard'))

if __name__ == "__main__":
	app.run()