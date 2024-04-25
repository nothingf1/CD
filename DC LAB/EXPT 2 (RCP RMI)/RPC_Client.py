import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print("factorial of 3 is : %s" % str(proxy.factorial_rpc(3)))
print("factorial of 5 is : %s" % str(proxy.factorial_rpc(5)))
