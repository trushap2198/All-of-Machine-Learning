from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/scoresee/<name>')
def results(name):
	return render_template('scores.html', user=name)

@app.route('/score', methods = ['POST','GET'])
def score():
	if request.method == 'POST':
		usern= request.form['nm']
		return redirect(url_for('results', name = usern))
	else:
		usern= request.args.get('nm')
		return redirect(url_for('results', name = usern))

if __name__ == '__main__':
	app.run(debug= True)
