import socket

# selecting host and port
target_host = 'Domain.name'
target_port = 443
# creating socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting our socket to targeted host an domain
s.connect((target_host,target_port))

#sending data
s.send('GET/HTTP/1.1\r\nHost:domain.com\r\n\r\n')

#receving response
response = s.recv(4096)

#printing response
print(response)
