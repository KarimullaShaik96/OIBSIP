import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message)

        except:
            break

    if client in clients:
        index = clients.index(client)
        clients.remove(client)

        nickname = nicknames[index]
        nicknames.remove(nickname)

        print(f"{nickname} disconnected.")

        broadcast(f"{nickname} left the chat.".encode("utf-8"))

    client.close()


def receive_connections():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 50)
    print("       OIBSIP CHAT SERVER")
    print("=" * 50)
    print(f"Server running on {HOST}:{PORT}")
    print("Waiting for clients...\n")

    while True:

        client, address = server.accept()

        print(f"Connected: {address}")

        client.send("NICK".encode("utf-8"))

        nickname = client.recv(1024).decode("utf-8")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")

        broadcast(f"{nickname} joined the chat!".encode("utf-8"))

        client.send("Connected to the chat server.".encode("utf-8"))

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


if __name__ == "__main__":
    receive_connections()