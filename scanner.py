import nmap

print("------------------------------------------ \n")
print("----------SCANNER-DO-EIKINHO-------------- \n")
ip = input("Digite o IP: ")
port_begin = input("Porta incial: ")
port_end = input("Porta final: ")

scanner = nmap.PortScanner()
print("------------------------------------------ \n")

for port in range(int(port_begin), int(port_end)+1):
    
    nmap_scanned = scanner.scan(ip, f"{port}")
    
    tcp = nmap_scanned["scan"][ip]["tcp"]
    state = tcp[port]["state"]
    name = tcp[port]["name"]

    if state == "open":
        print(f"PORT: {port} | STATE: {state} | SERVICE: {name}")
        print("------------------------------------------ \n")
