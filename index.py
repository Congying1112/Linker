from flask import render_template,Flask
from model import catalog, page_header


app = Flask(__name__)

@app.route('/')
def index():
	ph = page_header.ClsPageHeader("Elaine's")
	cat = catalog.ClsCatalog()
	month_list = 'Feb 2014', 'June 2014'
	comment_list = 'comm test1', 'comm test2'
	return render_template('tech.html', page_header = ph, catalog=cat, month_list = month_list, comment_list = comment_list)
	#return render_template('index2.html')

@app.route('/tech/')
def tech():
	cat = catalog.ClsCatalog()
	month_list = 'Feb 2014', 'June 2014'
	comment_list = 'comm test1', 'comm test2'
	return render_template('tech.html', catalog=cat, month_list = month_list, comment_list = comment_list)

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)