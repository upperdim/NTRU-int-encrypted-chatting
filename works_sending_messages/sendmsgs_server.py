import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1243))
s.listen(5)

con,addr = s.accept()
print("connected with ",addr)

# I can message back and forth 1 by 1 which is enough
while True:
    messg = input("send message to client: ")
    con.send(messg.encode())

    print("waiting for response")
    c_messg = con.recv(1024)
    print("message from client: ",c_messg.decode())