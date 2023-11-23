import socket
import threading

common_ports = {
    1: "TCPMUX",
    4: "UDP",
    5: "RJE",
    7: "ECHO",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    443: "HTTPS",
    135: "RPC",
    139 : "NetBios",
    143: "IMAP",
    161: "SNMP",
    443: "SSL",
    445 : "SMB",
    514 : "SYSLOG",
    3306 : "MySQL",
    3389 : "RDP",
}

def port_scan(target, port, open_ports):
    try:
        with socket.create_connection((target, port), timeout=1) as sock:
            open_ports.append((port, common_ports.get(port, "Port Tanımlanmadı")))
    except (socket.error, socket.timeout):
        pass

def main():
    target = input("Taramak İstediğiniz IP Adresini Giriniz: ")
    user_input = input("Port Aralığı Belirlemek İstiyor Musunuz? (e/h): ").lower()
    
    if user_input == 'e':
        start_port = int(input("Başlangıç Portunu Giriniz: "))
        end_port = int(input("Bitiş Portunu Giriniz: "))
        ports_range = range(start_port, end_port + 1)
    else:
        ports_range = range(1, 4000)

    threads = []
    open_ports = []
    
    for port in ports_range:
        thread = threading.Thread(target=port_scan, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Açık Portlar:")
    for port, service in open_ports:
        print(f"Port {port}: {service}")

if __name__ == "__main__":
    main()
