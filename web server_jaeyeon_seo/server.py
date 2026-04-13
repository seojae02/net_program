from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    try:
        request_line = req[0].split(' ')
        filename = request_line[1].lstrip('/') 
        
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html; charset=utf-8'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        else:
            raise FileNotFoundError

        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n\r\n'
        c.send(header.encode())

        response_data = f.read()
        if filename == 'index.html':
            c.send(response_data.encode())
        else:
            c.send(response_data)
        
        f.close()

    except (FileNotFoundError, IndexError):
        print(f"File Not Found: {filename}")
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        body += '<BODY>Not Found</BODY></HTML>'
        c.send(header.encode() + body.encode())

    c.close()