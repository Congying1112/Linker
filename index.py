from flask import render_template,Flask

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)