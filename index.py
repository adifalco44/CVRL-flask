from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
	return render_template('intro.html')


@app.route('/team')
def team_page():
	return render_template('team.html')


@app.route('/quiz_intro')
def quiz_intro_page():
	return render_template('quiz_intro.html')
