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
	print("\nrequest_data.decode(''utf-8\'):\'"+request_data.decode('utf-8')+"\'\n")

	filename = 'noURL.html'
	print("client_address: ", client_address)
	request_data_split = request_data.decode('utf-8').split(" ")
	print("request_data.decode('utf-8').split(" ")[1]:'"+request_data_split[1].replace("?", "")+"'")
	if request_data_split[1][0] == '/':
		print("Kautta")
		filename = request_data.decode('utf-8').split(' ')[1].split('/')[1].replace("?", "")
		print(filename)
	print('request_data_split[0]',request_data_split[0])

	if request_data_split[0] == 'POST':
		print("\033[95mLähetti Dataa\033[0m")
	else:
		print("\033[94mEi Lähettäny Dataa\033[0m")
#		try:
#			if ".." in filename:
#				file = open('nono.html')
#				http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
#				file.close()
#
#			else:
#				fileChats = open('chats/'+filename.split('/')[0], "r")
#				fileUpperHalf = open('upperHalf', "r")
#				fileBottomHalf = open('bottomHalf', "r")
#				
#				chats = fileChats.read()#.replace("\n", "<br>")
#				upperHalf = fileUpperHalf.read()
#				bottomHalf = fileBottomHalf.read()
#
#				http_response = bytes("HTTP/1.1 200 OK\n\n"+upperHalf+"\'"+chats+"\'"+bottomHalf,'utf-8')
#				print("chats.read():'"+chats+'\'')
#				fileChats.close()
#				fileUpperHalf.close()
#				fileBottomHalf.close()
#		except IOError:
#			http_response = b"""\
#HTTP/1.1 200 OK \n\n<html> <head> <title>Moi</title> </head> <body style='background-color: black;'> <h1 style='color: magenta;'>Not found</h1> </body> </html>"""


	if filename == 'noURL.html':
		file = open('noURL.html')
		http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
	else:
		# print("\033[95mMOI\033[m")
		try:
			if ".." in filename:
				file = open('nono.html')
				http_response = bytes("HTTP/1.1 200 OK\n\n"+(file.read()),'utf-8')
				file.close()

			else:
				fileChats = open('chats/'+filename.split('/')[0], "r")
				fileUpperHalf = open('upperHalf', "r")
				fileBottomHalf = open('bottomHalf', "r")
				
				chats = fileChats.read()#.replace("\n", "<br>")
				chatsList = ""
				for line in chats.split("\n"):
					chatsList+="<p>"+line.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;")+"</p>"
				upperHalf = fileUpperHalf.read()
				bottomHalf = fileBottomHalf.read()

				http_response = bytes("HTTP/1.1 200 OK\n\n"+upperHalf+chatsList+bottomHalf,'utf-8')
				print("chats.read():'"+chatsList+'\'')
				fileChats.close()
				fileUpperHalf.close()
				fileBottomHalf.close()
		except IOError:
			http_response = b"""\
HTTP/1.1 200 OK \n\n<html> <head> <title>Moi</title> </head> <body style='background-color: black;'> <h1 style='color: magenta;'>Not found</h1> </body> </html> """

	client_connection.sendall(http_response)
	client_connection.close()
