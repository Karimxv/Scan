import socket

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_ip = input("Entrez l'adresse IP à scanner: ")
    start_port = int(input("Entrez le port de départ: "))
    end_port = int(input("Entrez le port de fin: "))

    print(f"Scanning {target_ip} de {start_port} à {end_port}...")
    open_ports = scan_ports(target_ip, start_port, end_port)
    
    if open_ports:
        print(f"Ports ouverts sur {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"Aucun port ouvert trouvé sur {target_ip} dans la plage spécifiée.")
