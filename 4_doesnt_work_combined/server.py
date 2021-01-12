import socket
import time
import pickle
from ntru import *

HEADERSIZE = 10

# these are for NTRU encryption
q = 122430513841
f = 231231
g = 195698

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

con, addr = s.accept()
#print("Connected to ", addr).
print("Connected") # dont show ip or adresses

while True:
    # send message
    msg = input("Send message to client: ") # input str
    enc = encrypt_message(msg, q, f, g) # inputs str, returns int array
    sendthis = pickle.dumps(enc)
    sendthis = bytes(f"{len(sendthis):<{HEADERSIZE}}", 'utf-8')+sendthis
    con.send(sendthis)

    # recieve message
    print("Wating for reply...")
    full_msg = b''
    new_msg = True
    while True:
        msg = con.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if (len(full_msg) - HEADERSIZE == msglen):
            # recieved encrypted int array
            enc = pickle.loads(full_msg[HEADERSIZE:])
            #print(enc)
            # decrypted string
            dec = decrypt_message(enc, q, f, g)
            print(dec)
            break 
