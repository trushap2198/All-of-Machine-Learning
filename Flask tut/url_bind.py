from flask import Flask #import the Flask module
app = Flask('__name__') #takes name of cuurent module as argument

@app.route('/hello') #runs with http://127.0.0.1:5000/hello as hello url binds with hello function
def hello():
	return "hello world_ with url bind to function!"
#can also use -app.add_url_rule(‘/’, ‘hello’, hello) - add_url_rule('/',url_name,func_name)
if __name__=='__main__': 
	app.run(debug=True)
 