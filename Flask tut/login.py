from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
	return render_template('hello.html', name= user) #login.py is in same folder as templates and hello.html is in templates

@app.route('/login', methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		usern= request.form['nm']
		return redirect(url_for('hello_name', user = usern))
	else:
		usern= request.args.get('nm')
		return redirect(url_for('hello_name', user = usern))

if __name__ == '__main__':
	app.run(debug= True)	