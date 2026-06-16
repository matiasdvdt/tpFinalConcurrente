import socket 
import threading 
 
def intentar_comprar(id_cliente): 
    try: 
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        cliente.connect(('127.0.0.1', 5555)) 
        cliente.send("COMPRAR".encode('utf-8')) 
         
        respuesta = cliente.recv(1024).decode('utf-8') 
        print(f"[Cliente {id_cliente}] Respuesta: {respuesta}") 
         
    except Exception as e: 
        print(f"[Cliente {id_cliente}] Error de conexión: {e}") 
    finally: 
        cliente.close() 
 
print("Iniciando venta masiva...") 
 
# Disparamos 10 hilos concurrentes para agotar las 5 entradas 
hilos_clientes = [] 
for i in range(1, 11): 
    hilo = threading.Thread(target=intentar_comprar, args=(i,)) 
    hilos_clientes.append(hilo) 
    hilo.start() 
 
for hilo in hilos_clientes: 
    hilo.join() 
 
print("Prueba de estrés finalizada.") 