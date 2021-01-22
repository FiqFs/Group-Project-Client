import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.193', 1233))
response = client.recv(32)

name = input(response.decode())	
client.send(str.encode(name))
response = client.recv(32)

password = input(response.decode())	
client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''

response = client.recv(32)
response = response.decode()

print(response)
client.close()
