from flask import render_template,Flask

app = Flask(__name__)

@app.route('/')
@app.route('/timeline/')
def timeline():
    return render_template('Timeline/timeline.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)