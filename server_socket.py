import socket


def run(server_address):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    server_socket.listen()

    connections = []

    try:
        while True:
            connection, client_address = server_socket.accept()
            print(f'connection request received from {client_address}')
            connections.append(connection)

            for connection in connections:
                buffer = b''

                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data: break
                    else:
                        print(f'data received {data}')
                        buffer = buffer + data
                print(f'all data: {buffer}')

                connection.send(buffer)
    finally:
        server_socket.close()


if __name__ == '__main__':
    run(('127.0.0.1', 8000))
