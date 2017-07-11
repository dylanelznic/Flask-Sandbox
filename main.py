from flask import Flask, render_template
from dummy_script import print_to_console

app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

if __name__ == "__main__":
	app.run()