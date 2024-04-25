import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5050))  # Using port 5050 instead of 25
server.listen(1)
print('Server listening on port 5050...')

while True:
    conn, addr = server.accept()
    print('Connection from:', addr)
    sum_result = 0
    
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'stop':
            break
        sum_result += int(data)
        conn.send(str(sum_result).encode('utf-8'))
        
    conn.close()
    print('Connection closed.')

server.close()
