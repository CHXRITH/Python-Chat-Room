import socket
import threading

def handle_client(client_socket):
    client_name = client_socket.recv(1024).decode('utf-8')
    print(f"Client {client_name} has connected.")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Client {client_name} has disconnected.")
            break
        message = data.decode('utf-8')
        print(f"Received message from {client_name}: {message}")
        response = f"Server received your message, {client_name}: {message}"
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
