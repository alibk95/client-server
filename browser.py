import socket
# creates a socket object and the first argument is the internet protocol type the socket is using(IPv4) and
# the second argument basically shows the TCP protocol that is used to transfer our messages on network level.
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")
# indicate the URL and the port to connect the so called phone call
socket_obj.connect(('127.0.0.1', 9010))
# the encode is there cause the data format inside python is in Unicode whereas outside on the internet is
# UTF-8 so we simply use the encode() method to handle this issue
command = 'GET http://127.0.0.1 HTTP/1.0\r\n\r\n'.encode()
socket_obj.send(command)
while True:
    data = socket_obj.recv(1024)
    if len(data) < 1:
        break
    print(data.decode())

# after the data is completely received from the server it is better to drop the socket connection
# because we don't want to end up having bunch of half dropped connections piling up.
socket_obj.close()
