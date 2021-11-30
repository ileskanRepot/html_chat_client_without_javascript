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
	print("\nrequest_data.decode('utf-8'):",request_data.decode('utf-8'))

	filename = 'noURL.html'

	print('\''+request_data.decode('utf-8')[5]+'\'')
	if request_data.decode('utf-8')[5] == '?':
		print("Kyssäri")
		filename = request_data.decode('utf-8').split(' ')[1].split('?')[1]
		print(filename)

	if filename == 'noURL.html':
		file = open('noURL.html')
		http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
	else:
		try:
			if ".." in filename:
				file = open('nono.html')
				http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
			else:
				file = open('chats/'+filename.split('/')[0])
				http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
			file.close()
		except IOError:
			http_response = b"""\
HTTP/1.1 200 OK

<html>
	<head>
		<title>Moi</title>
	</head>
	<body style='background-color: black;'>
		<h1 style='color: magenta;'>Not found</h1>
	</body>
</html>
"""
	client_connection.sendall(http_response)
#	request_data = client_connection.recv(1024)
	client_connection.close()
