import xmlrpc.server

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Change the port for multiple servers
port = 8002
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', port))
server.register_function(factorial)
print(f"Server started on http://localhost:{port}")
server.serve_forever()
