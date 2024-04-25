import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5050))  # Connect to port 5050
while True:
    send_data = input('Send: ')
    client.send(send_data.encode('utf-8'))
    if send_data == 'stop':
        break
    response = client.recv(1024).decode('utf-8')
    print('Reply:', response)

client.close()
