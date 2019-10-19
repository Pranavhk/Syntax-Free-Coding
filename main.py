# import Flask
from flask import Flask, render_template, flash, request
from naive_classifier import nb_classifier
import Translator_basic
import subprocess
import sys
import os

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])

def apphome():
	code = list()
	flag = 0
	if(request.method == 'GET') :
		return render_template("app_home.html")
	if(request.method == 'POST') :
		if 'convert' in request.form :
			text = request.form['text']
			if os.path.isfile("Voice_Code_Output.py") and os.path.getsize("Voice_Code_Output.py") > 0 :
				f = open("Voice_Code_Output.py","a+")
			else :
				f = open("Voice_Code_Output.py","w+")
			intent = nb_classifier(text,f)
			f.close()
			code = get_code()
			return render_template("app_home.html",intent = intent, code = code,flag =flag)	

		elif 'run' in request.form :
			output = "File Empty or doesnt exist"
			try:
				if os.path.isfile("Voice_Code_Output.py") and os.path.getsize("Voice_Code_Output.py") > 0 :
					result = subprocess.check_output('python Voice_Code_Output.py', shell=True)
					output=result.decode(sys.stdout.encoding)
			except subprocess.CalledProcessError as e:
				output = "Failed"
			print("output is: ")
			print(output)
			code = get_code()
			return render_template("app_home.html",output = output,code = code,flag=flag)

		elif 'newfile' in request.form :
			open('Voice_Code_Output.py', 'w').close()
			return render_template("app_home.html")

def get_code():
	code = list()
	with open("Voice_Code_Output.py", 'r') as f:
				line = f.readline()
				while line:
					code.append(line.rstrip('\n'))
					line = f.readline()
				return code

if __name__ == "__main__":
	app.run(debug=True, port=8080, threaded=True)