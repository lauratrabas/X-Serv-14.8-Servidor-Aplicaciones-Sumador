#!/usr/bin/python

#Laura Trabas Clavero

import socket


class webApp:
	
	def parse(self, request):
		return None

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>It works!</h1></body></html>")
        
	def __init__(self, hostname, port):
        
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		mySocket.bind((hostname, port))
		mySocket.listen(5)
        
		numero1 = None
		
		while True:
			print 'Waiting for connections'
			(recvSocket, address) = mySocket.accept()
			print 'HTTP request received (going to parse and process):'
			request = recvSocket.recv(2048)
			print request
			parsedRequest = self.parse(request)
			(returnCode, htmlAnswer, numero1) = self.process(parsedRequest, numero1)
				
			print 'Answering back...'
			recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n")
			recvSocket.close()
class Sumador(webApp):

	def parse(self,request):
		entero = int(request.split(' ')[1][1:])
		return entero
		
	def process(self, parsedRequest,numero1):
		if numero1 == None:
			numero1 = parsedRequest
			htmlAnswer = "<html><body>" + "Primer numero es:" + str(numero1) +"</p>" + "Dame otro numero" + "</body><html>"
		else:
			resultadosuma = str(numero1 + parsedRequest)
			htmlAnswer = "<html><body>" + "El resultado de la suma es: " + str(resultadosuma) + "</body><html>"
			numero1 = None
		return ("HTTP/1.1 200 OK", htmlAnswer, numero1)

if __name__ == "__main__":
	testWebApp = Sumador("localhost", 1234)
