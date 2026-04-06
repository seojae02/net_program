from socket import *

port = 3333
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

while True:
    conn, addr = s.accept()

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            expression = data.decode()
            if expression.lower() == 'q':
                break

            print(f"Received message: {expression}")

            result = eval(expression)
            
            if isinstance(result, float):
                formatted_result = f"{result:.1f}"
            else:
                formatted_result = str(result)

            conn.send(formatted_result.encode())

        except Exception as e:
            conn.send(b"Try again")
            
    conn.close()