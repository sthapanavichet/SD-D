import socket
import threading

users = {}
client_sockets = {}


def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    return False


def client_handler(client, address):
    try:
        request = client.recv(1024).decode('utf-8')
        choice, login_info = request.split(",")
        username, password = login_info.split(':')

        if choice.upper() == 'S':
            users[username] = password
            client_sockets[username] = client
            client.send('Success'.encode('utf-8'))
        elif choice.upper() == 'L':
            if authenticate(username, password):
                client_sockets[username] = client
                client.send('Success'.encode('utf-8'))
            else:
                client.send(f'Fail'.encode('utf-8'))

        while True:
            user = client.recv(2048).decode('utf-8')
            if user in client_sockets:
                client.send('Success'.encode('utf-8'))
                break
            else:
                client.send('Fail'.encode('utf-8'))

        while True:
            message = client.recv(2048)
            user_client = client_sockets[user]
            user_client.send(message)

    except(socket.error, ValueError, ConnectionResetError):
        # Handle disconnection or errors here
        user_close = None
        for username, user_socket in client_sockets.items():
            if user_socket == client:
                user_close = username
        if user_close:
            del client_sockets[user_close]
        print(f"Connection with {address} closed.")


def send_message(message, user):
    user_socket = client_sockets[user]
    user_socket.send(f"{user}: {message}".encode('utf-8'))


def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))
    except:
        print("Server couldn't start")
    print("Server started.")
    server.listen(10)

    while True:
        client, address = server.accept()
        print(f"Successfully connected to {address}")
        client_handler_thread = threading.Thread(target=client_handler, args=(client, address), daemon=True).start()


if __name__ == '__main__':
    main()
