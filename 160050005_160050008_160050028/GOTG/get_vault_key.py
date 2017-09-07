from urllib import request, parse

dataDictionary = {'identity':'Star-Lord', 'password':'TheOrbIsMine'}
dataEncoded = parse.urlencode(dataDictionary).encode()
req = request.Request("https://www.cse.iitb.ac.in/~rohitrango/outlab/entrance.php", data = dataEncoded)
response = request.urlopen(req)
a = response.read().decode('utf-8')
print("The message returned on sending the POST request was:")
print(a)
print()
print("And the key is hence:")
print(a[-32:])