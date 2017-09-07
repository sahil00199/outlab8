from zipfile import ZipFile 
import os

name = "final_message.zip"
file = open("words.txt", 'r')
zip = ZipFile(name)
for line in file:
	try:
		zip.extractall(pwd = line.split()[0].encode('utf-8'))
		print(line)
		break
	except:
		#print("not :" , line)
		continue