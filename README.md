# Servidor y Cliente TCP en Python

Este proyecto implementa un **servidor y cliente TCP** en Python.  
El servidor puede manejar múltiples clientes y cierra la conexión si recibe el mensaje `"DESCONEXION"`, pero sigue disponible para nuevos clientes.  
El cliente permite al usuario enviar mensajes al servidor y se desconecta si se envía `"DESCONEXION"`.

## 🚀 Requisitos
- Python 3.x

## 📦 Instalación y Uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/DavidRuizJR/Servidor_TCP.git
cd servidor-tcp

### 2️⃣ Ejecutar el servidor
```bash
python servidor.py

### 3️⃣ Ejecutar el cliente
```bash
python cliente.py
El cliente pedirá un mensaje.
Si escribes "DESCONEXION", el cliente se cerrará.



