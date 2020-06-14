from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from textblob import TextBlob

# load the model from disk
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/analyse',methods=['POST'])
def predict():
	if request.method == 'POST':
		customText = request.form['customText']
		userinput = request.form['userinput']
		if customText is '':
			message=userinput
		else:
			message=customText

		analysis = TextBlob(message)
		polarity=analysis.sentiment[0]
		if polarity<0:
			my_prediction = -1
		elif polarity==0:
			my_prediction = 0
		else:
			my_prediction = 1

	return render_template('index.html',prediction=my_prediction,yourtext=message)


if __name__ == '__main__':
	app.run(debug=True)