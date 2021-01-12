import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1243))

# I can message back and forth 1 by 1 which is enough
while True:
    print("wating for response")
    s_messg=s.recv(1024)
    print("message from server: ",s_messg.decode())
    
    c_messg=input("send message to server: ")
    s.send(c_messg.encode())