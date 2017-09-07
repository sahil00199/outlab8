from generator import *			# you need to implement this
from hashlib import md5
SECRET_KEY = 42				# the answer to everything

g = nextNumberGenerator()
l = []
for i in range(SECRET_KEY):
	l.append(str(next(g)))

# DO NOT change anything in this file

l = "".join(map(lambda x: md5(x.encode()).hexdigest(), l))
l = (md5(l.encode()).hexdigest())
with open('eye.txt', 'w') as eye:
	eye.write(l+"\n")


