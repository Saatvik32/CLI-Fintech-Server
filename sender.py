import socket

def main():
    host = '127.0.0.1'  # Server IP
    port = 3000

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server started")

    while True:
        conn, addr = server_socket.accept()
        print("Client connected from:", addr)

        with open('output.csv', 'rb') as file:
            data = file.read()

        conn.sendall(data)
        print("File sent")

        conn.close()

if __name__ == '__main__':
    main()
