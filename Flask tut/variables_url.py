from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:stuid>')
def show_id(stuid):
	return 'int id: %d' %stuid #run as http://127.0.0.1:5000/blog/16
@app.route('/rev/<float:percentage>')
def show_perc(percentage): # run as http://127.0.0.1:5000/rev/97.0
	return 'Percentage: %f' %percentage
@app.route('/python/')
def hello_python(): #run as http://127.0.0.1:5000/python or '/python/'
	return 'Hello_Python'
@app.route('/modules')
def hello_modules():
	return 'hello modules' #run as http://127.0.0.1:5000/modules
if __name__ == '__main__':
	app.run()
