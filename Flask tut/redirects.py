from flask import Flask,redirect,url_for
app= Flask('__name__')

@app.route('/admin')
def hello_admin():
	return 'hello admin'

@app.route('/student/<name>') #http://127.0.0.1:5000/user/admin
def student(name):
	return 'Hello student:%s' %name

@app.route('/user/<name>')
def user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('student',name=name)) # http://127.0.0.1:5000/user/student_name

if __name__ == '__main__':
	app.run(debug = True)


