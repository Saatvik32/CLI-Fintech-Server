import socket

def main():
    host = '127.0.0.1'  # Server IP
    port = 3000

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data = b''
    while True:
        packet = client_socket.recv(4096)
        if not packet:
            break
        data += packet

    with open('received_file.csv', 'wb') as file:
        file.write(data)

    print("File received")

    client_socket.close()

if __name__ == '__main__':
    main()
