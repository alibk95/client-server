from socket import *

HOST = '127.0.0.1'
PORT = 9010
def start_server():
    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((HOST, PORT))
    # handles up to 3 calls, not at the same time but saves them somewhere so that whenever the current connection is
    # closed then connects to the next one.
    socket_obj.listen(3)
    while(1):
        # server waits at tj=his line and listens on the port till the client wants to connect.
        (client_socket, address) = socket_obj.accept()
        # read the command that is send from the client (in this case it's a simple GET request!)
        # decode it cause the data inside python is in Unicode format and outside in between the sockets is UTF-8
        dt = client_socket.recv(5000).decode()
        dt_splitted = dt.split("\n")
        # print the command received from client
        if len(dt_splitted) > 0:
            print(dt_splitted[0])
        # data that server provides to send to the client
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        data += "<html><body>Hey Hey Hey</body></html>\r\n\r\n"
        client_socket.sendall(data.encode())
        # after sending the data the connection needs to be closed according to the protocol
        # if we don't do it the server keeps listening on the port.
        client_socket.shutdown(SHUT_WR)
        socket_obj.close()

print('Access http://127.0.0.1:9010')
start_server()