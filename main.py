from flask import Flask
from dummy_script import print_to_console

app = Flask(__name__)

@app.route('/')
def landing_page():
	return 'Hello'

if __name__ == "__main__":
	app.run()