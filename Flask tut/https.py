from flask import Flask, redirect, url_for, request
app = Flask('__name__')

@app.route('/success/<name>')
def success(name):
	return 'welcome user name: %s' %name

@app.route('/register', methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		usern = request.form['nm']
		return redirect(url_for('success',name= usern)) #here name attribute is the vlaue from /success/<name>
	else:
		usern= request.args.get('nm')
		return redirect(url_for('success',name= usern))

if __name__ == '__main__':
	app.run(debug = True)	

#runt the script
#open login.html as file:///D:/Flask%20tut/login.html from browser
#click submit
#redirected to http://localhost:5000/success/trusha
