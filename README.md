                            # ssh-login-bruteforcing
                           
This Python script is a simple SSH brute force tool designed to automate the process of attempting to login to an SSH server by trying different combinations of usernames and passwords.

                              Description
The script reads a list of usernames and passwords from a text file and attempts to establish an SSH connection to a specified host using each combination of credentials. It makes use of the paramiko library for SSH connections and the pwn library for interactive terminal functionalities.

                              Usage
Clone the repository or download the ssh.py script.

Make sure you have Python installed on your system.

Edit the bruteforce_ssh.py file and specify the target host IP address or hostname, as well as the username and path to the file containing the list of passwords (baba.txt in this case).
Run the script using Python:

python ssh.py

The script will start attempting to login to the SSH server using the provided credentials. If a successful login is found, it will print the password and exit.

                               Requirements
                               
Python 3.x

paramiko

pwn

                                Disclaimer
This tool is for educational purposes only. Unauthorized access to computer systems is illegal and unethical. Use this tool responsibly and only on systems you are authorized to test.

