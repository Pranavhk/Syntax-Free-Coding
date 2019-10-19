import json
import os
from collections import Counter
json_data = Counter

def data_to_json(intent,datadict, file_name) :
	if os.path.isfile(file_name) and os.path.getsize(file_name) > 0 :

		with open(file_name, 'r') as f:
			data = json.load(f)
		
		if intent in data :
				#print("modify")
				with open(file_name, 'r+') as f:
					json_data = json.load(f)
					json_data[intent] = dict(Counter(json_data[intent]) + datadict)
					f.seek(0)
					f.write(json.dumps(json_data))
					f.truncate()
		else :
			#print("append")
			with open(file_name) as f:
				data = json.load(f)
			data.update(dict({intent : datadict}))
			with open(file_name, 'w') as f:
				json.dump(data, f)
	else:
		with open(file_name, 'w') as f:
			#print("file created")
			json.dump(dict({intent : datadict}), f)

def intent_count(file_name) :
	if os.path.isfile(file_name) and os.path.getsize(file_name) > 0 :
		with open(file_name, 'r') as f:
			data = json.load(f)
			count = len(data.keys())	
		return count

	else:
		print("Error: File not found")

def json_to_data(file_name) :
	if os.path.isfile(file_name) and os.path.getsize(file_name) > 0 :
		with open(file_name, 'r') as f:
				data = json.load(f)
		return data


def save_sentence(intent,sentence,result) :
	if result == 1 :
		if os.path.isfile("correct_sentences"):
			with open("correct_sentences", 'a') as f:
				f.write("\n"+sentence+" $"+intent)

		else:
			with open("correct_sentences", 'w') as f:
				f.write("\n"+sentence+" $"+intent)
	else:
		if os.path.isfile("wrong_sentences"):
			with open("correct_sentences", 'a') as f:
				f.write("\n"+sentence+" $"+intent)

		else:
			with open("wrong_sentences", 'w') as f:
				f.write("\n"+sentence+" $"+intent)
