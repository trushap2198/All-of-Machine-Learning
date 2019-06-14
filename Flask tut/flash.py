from flask import Flask, render_template, request,url_for,flash, redirect
app= Flask(__name__) #dont apostrophe it
app.secret_key = 'random string'

@app.route('/')
def index():
	return render_template('flashindex.html')

@app.route('/flashlogin',methods=['POST','GET'])
def login():
	error = None

	if request.method == 'POST':
		if request.form['username'] != 'admin' or \
		   request.form['password'] != 'admin':
		   error = 'Invalid POST'
		else:
			flash('you were successfully logged in')
			return redirect(url_for('index'))
	return render_template('flashlogin.html', error = error)

if __name__ == '__main__':
	app.run(debug = True)