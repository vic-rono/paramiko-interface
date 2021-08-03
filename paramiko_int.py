import paramiko
import time
import getpass

ip_address = input("IP Address:") or "10.10.10.1"
username = input("Username:") or "v_rono"
password = getpass.getpass() or "router_1"
 
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"Success login to {ip_address}")
conn = ssh_client.invoke_shell()

conn.send("conf t\n")

for x in range(0,4):
    conn.send(f"int lo{x}\n")
    conn.send(f"ip add 10.1.1.{x+1} 255.255.255.255\n")
    time.sleep(1)

output = conn.recv(65535).decode()
print(output)

ssh_client.close()

#run python3 paramiko_int.py in the remote ubuntu server
#do show ip int brief on the router
