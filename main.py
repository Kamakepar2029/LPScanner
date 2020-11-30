import threading
from gen import generate
from gen import generation
import socket
from colorama import Fore
from datetime import datetime
import os
pstart = datetime.now()
print(pstart)
os.system('rm ips.txt')
generate(10)
#generation(512)
def scan_port(ip,port):
  start = datetime.now()
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip,port))
     print(Fore.GREEN + 'Port :',port,' is open.')
     os.system('echo "'+str(ip)+'">>logs.txt')
     os.system('echo "[+] Port Opened">>logs.txt')
     connect.close()
  except:
     print(Fore.RED + 'Port :',port,' is not open')
     pass

myips = []
ips = str(input('Enter ip to scan: '))
myips.append(ips)
start = 0
end = len(myips)
while start<end:
   ip = myips[start]
   print(ip)
   os.system('echo "IP: '+ip+'">>log.txt')
   for i in range(1000):
      potoc = threading.Thread(target=scan_port, args=(ip,i))
      potoc.start()
   start+=1

pends = datetime.now()
print('Time : {}'.format(pends-pstart))
