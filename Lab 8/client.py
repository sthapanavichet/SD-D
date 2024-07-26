import socket
import threading


def server_response(response):
    if response == 'Success':
        return True
    elif response == 'Fail':
        return False


def receive_message(server):
    while True:
        message = server.recv(1024).decode('utf-8')
        print(f"\r{message}" + " " * len("Enter the message:")+ "\nEnter the message: ", end='')


def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    print('Successfully connected to server.')

    choice = input("Enter S to Sign up and L to Login in: ")

    if choice.upper() == 'S':
        username = input('Enter name for the new user: ')
        password = input('Enter password: ')
    elif choice.upper() == 'L':
        username = input('Enter username: ')
        password = input('Enter password: ')
    else:
        print("Invalid Choice")
        return 0

    server.send(f"{choice.upper()},{username}:{password}".encode('utf-8'))
    response = server.recv(1024).decode('utf-8')
    if server_response(response):
        print('You have been successfully logged in.')
    else:
        print('username or passowrd is incorrect. Try again')
        return 0
    while True:
        user_request = input("Enter the user you want to chat with: ")
        server.send(f"{user_request}".encode('utf-8'))
        response = server.recv(1024).decode('utf-8')
        if server_response(response):
            print(f'Successfully connected to {user_request}.')
            break
        else:
            print(f'Connection to {user_request} failed.')

    print("To stop chatting, enter Q")
    receive_message_thread = threading.Thread(target=receive_message, args=(server,), daemon=True).start()

    while True:
        message = input("Enter the message: ")
        if message.upper() == 'Q':
            break
        server.send(f"{username}: {message}".encode('utf-8'))
        print(f"{username}: {message}")


if __name__ == '__main__':
    main()
