import socket

HOST = "127.0.0.1"  # Dirección del servidor
PORT = 5000
def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:
            message = input("Escribe un mensaje: ")
            client_socket.sendall(message.encode("utf-8"))

            if message.strip().upper() == "DESCONEXION":
                print("Desconectando del servidor...")
                break  # Termina el cliente

if __name__ == "__main__":
    start_client()
