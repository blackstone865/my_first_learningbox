
import socket

target = "baidu.com"
ports = [21, 22, 23, 80, 443, 3306, 8080]

service_names = {
    21: "FTP(文件传输)",
    22: "SSH(远程控制)",
    23: "Telnet(远程控制)",
    80: "HTTP(网页)",
    443: "HTTPS(加密网页)",
    3306: "MySQL(数据库)",
    8080: "HTTP代理"
}

print(f"正在扫描目标 {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        service = service_names.get(port, "未知服务")
        print(f"端口 {port}: 开放 → {service}")
    else:
        print(f"端口 {port}: 关闭")
    
    sock.close()
