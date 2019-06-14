from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME']='trushap2198@gmail.com'
app.config['MAIL_PASSWORD']='thejaggernaut'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
	msg = Message('Hello', sender = 'trushap2198@gmail.com', recipients=['bindiyacool@gmail.com','bindiyapatel18@yahoo.com'])
	msg.body = 'HELLO flask message to you'
	msg.attach('errors.jpg','image/jpg',)
	mail.send(msg)
	return 'Mail sent'

if __name__ == '__main__':
	app.run(debug = True)