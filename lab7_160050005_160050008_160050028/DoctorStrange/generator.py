import itertools
final = ''
count = -1
value ='' 

def nextNumberGenerator():
	val = 1
	while True:
		yield val
		val = valueCalc(val)

def valueCalc(val):
	global value
	global final
	global count
	dummy=list(itertools.takewhile(pred, list(str(val))))
	final += str(count+1) + str(value)
	count = -1
	alpha = int(final)
	final = ''
	return alpha

def pred(c):
	global value
	global final
	global count
	if c == value:
		count = count + 1
	else:
		if count >=0:	
			final += str(count+1) + str(value)
		
		count = 0 
		value = c
	return True;	
