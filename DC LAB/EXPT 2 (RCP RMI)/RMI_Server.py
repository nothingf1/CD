import Pyro4

@Pyro4.expose
class RemoteObject:
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, x, y):
        return x + y
daemon = Pyro4.Daemon()
uri = daemon.register(RemoteObject)
print(f"Server object URI: {uri}")
daemon.requestLoop()


#Remember to run the server first. The URI you get after running the server should be copied and pasted into the Client code