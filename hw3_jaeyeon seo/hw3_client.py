from socket import *

s = socket(AF_INET, SOCK_STREAM)
address = ("localhost", 3333)

try:
    s.connect(address)

    while True:
        msg = input("계산식을 입력하세요: ")

        if msg.lower() == 'q':
            s.send(b'q')
            break

        if not msg.strip():
            continue

        s.send(msg.encode())

        result = s.recv(1024).decode()
        print(f"결과: {result}")

except Exception as e:
    print(f"Connection error: {e}")

finally:
    s.close()