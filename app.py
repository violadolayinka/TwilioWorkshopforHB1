#from the flask library, I've imported the Flask class
from flask import Flask
#from the twilio library, I've imported the Twiml class
from twilio import twiml

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
#Here, I've defined our function
def sms_reply():
	#create the Response object
	res = twiml.Response()
	#adding a message to the response
	res.message("Thanks for visiting Twilio! I hope you have a great visit.")
	#returning our response
	return str(res)

if __name__ == "__main__":
	app.debug = True
	app.run()
