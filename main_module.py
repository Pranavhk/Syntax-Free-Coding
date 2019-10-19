import naive_classifier as nc
import Translator_basic
import os
def main():
	open('Voice_Code_Output.py', 'w').close()
	while(1):
		print("\nEnter a command: ")
		sent = input()
		if sent == "switch off":
			break
		else :
			if os.path.isfile("Voice_Code_Output.py") and os.path.getsize("Voice_Code_Output.py") > 0 :
				f = open("Voice_Code_Output.py","a+")
			else :
				f = open("Voice_Code_Output.py","w+")
			a =nc.nb_classifier(sent,f)
			f.close()
	print("\nDo you want to see the output? (yes to view and no to exit)")
	ans = input()
	if ans == 'yes':
		print("Here is the output:- \n")
		f = open("Voice_Code_Output.py","r")		
		line = f.readline()
		cnt = 1
		while line:
			print("{}    {}".format(cnt, line.rstrip('\n')))
			line = f.readline()
			cnt += 1 			
		f.close()
		print ("\nDo you want to run this file? (yes to run and no to exit)")
		r = input()
		if r == 'yes':
			print("\tThe output is: \n")
			os.system('python Voice_Code_Output.py')
		elif r == 'no':
			return
		else:
			print("Invalid response")	
	elif ans == 'no':
		return
	else:
		print("Invalid response") 	

main()
