import socket
import threading


HOST = "0.0.0.0" # Este host para escuchar en todas las interfaces de red
PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def iniciar_servidor():
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    global server_socket
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Cliente conectado desde {client_address}")
                while True:
                    data = client_socket.recv(1024).decode("utf-8")
                    if not data:
                        break
                    print(f"Mensaje recibido: {data.upper()}")
                    
                    if data.strip().upper() == "DESCONEXION":
                        print(f"Cliente {client_address} desconectado.")
                        break  # Salir del bucle interno y cerrar solo este cliente
        except OSError:
                break


def cerrar_servidor():
    while True:
        cmd = input()
        if cmd.strip().upper() == "SALIR":
            print("Cerrando servidor...")
            server_socket.close()
            break


server_thread = threading.Thread(target=iniciar_servidor, daemon=True)
server_thread.start()

cerrar_servidor()