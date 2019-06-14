from flask import Flask
app = Flask('__name__')

@app.route('/helloarg/<name>')
def hello_user(name):
	return 'hello user %s!' %name

if __name__ == '__main__':
	app.run(debug=True)
#run as localhost:5000/helloard/<firstuser>