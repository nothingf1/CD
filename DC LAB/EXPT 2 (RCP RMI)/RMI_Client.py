import Pyro4

uri = "PYRO:obj_d98d11c3bdab42ecbb7bff6c7144a578@localhost:57249" 

#Replace with actual URI
with Pyro4.Proxy(uri) as proxy:
    print(proxy.greet("Bard"))
    result = proxy.add(4, 5)
    print(f"4 + 5 = {result}")


#Paste the obtained URI from the server here in client code