import socket

HOST, PORT = '', 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Serving HTTP on port {PORT} ...")
while True:
	client_connection, client_address = listen_socket.accept()
	request_data = client_connection.recv(1024)
	print("———\nrequest_data.decode('utf-8'):",request_data.decode('utf-8'),"———")

	# if request_data.decode('utf-8').split(" ")[0] == 'POST':
		

	filename = 'noURL.html'
	file = open(filename)
	http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
	client_connection.sendall(http_response)
	# request2_data = client_connection.recv(1024)
	client_connection.close()

	# print("\nrequest2_data.decode('utf-8'):",request2_data.decode('utf-8'))

	# client_connection.close()
