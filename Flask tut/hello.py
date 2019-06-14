from flask import Flask #import the Flask module
app = Flask('__name__') #takes name of cuurent module as argument

@app.route('/') #tells which url to call for the associated function
def hello():
	return "hello world!"

if __name__=='__main__': 
	app.run(debug=True)  #to run application on local server

