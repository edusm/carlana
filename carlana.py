#guilmour

import SocketServer
import SimpleHTTPServer

PORTA = 8787

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORTA), Handler)

print "Servidor criado na prota:", PORTA
httpd.serve_forever()
