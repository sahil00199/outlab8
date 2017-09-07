import os
import pathlib

def recurse():
	filesFolders = os.listdir()
	ans = ""
	#print(filesFolders)
	for file in filesFolders:
		#print(os.getcwd())
		if file == "key.txt":
			f = open(file)
			s = f.read()
			#print(s)
			if len(s.split(":")[-1].split()) > 0 and len(s.split(":")[-1].split()[0]) == 32:
				print("The complete path is:" + os.getcwd() + "/key.txt")
				print()
				return s
		else:
			os.chdir(file)
			ans = recurse()
			if len(ans) >= 32:
				return ans
	os.chdir(str(pathlib.Path(os.getcwd()).parent))
	return ""


if __name__=="__main__":
	og_path = os.getcwd()
	os.chdir('World')
	key  = recurse()
	print(key)
	os.chdir(og_path)
	file = open("key.txt",'w')
	file.write(key)
	file.close()