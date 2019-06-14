from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def student():
	return render_template('user.html')

@app.route('/user',methods = ['POST','GET'])
def book():
	if request.method == 'POST':
		userinfo = request.form
		return render_template('userinf.html', user= userinfo)

if __name__ == '__main__':
	app.run(debug = True)
	