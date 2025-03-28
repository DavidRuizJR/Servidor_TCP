import socket

HOST = "0.0.0.0" # Este host para escuchar en todas las interfaces de red
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Cliente conectado desde {client_address}")
                while True:
                    data = client_socket.recv(1024).decode("utf-8")
                    if not data:
                        break
                    print(f"Mensaje recibido: {data}")
                    
                    if data.strip().upper() == "DESCONEXION":
                        print(f"Cliente {client_address} desconectado.")
                        break  # Salir del bucle interno y cerrar solo este cliente

if __name__ == "__main__":
    start_server()
