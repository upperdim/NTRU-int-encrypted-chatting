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
print("Connected to ", addr)

while True:
    # send message
    msg = input("Send message to client: ") # input str
    enc = encrypt_message(msg, q, f, g) # inputs str, returns int array
    sendthis = pickle.dumps(enc)
    sendthis = bytes(f"{len(sendthis):<{HEADERSIZE}}", 'utf-8')+sendthis
    con.send(sendthis) # gotta send int array

    # recieve message
    print("Wating for reply...")
    full_msg = b''
    new_msg = True
    while True:
        msg = con.recv(16)
        if new_msg:
            #print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        
        #print(f"full message length : {msglen}")

        full_msg += msg

        #print(len(full_msg))

        if (len(full_msg) - HEADERSIZE == msglen):
            #print("Full message recieved")
            #print(full_msg[HEADERSIZE:]) # prints bytes in hex
            enc = pickle.loads(full_msg[HEADERSIZE:])
            #print(enc) # prints the int array
            dec = decrypt_message(enc, q, f, g)
            print(dec) # print the decrypted message
            new_msg = True
            full_msg = b""

    # print("Waiting for reply...")
    # recieved_msg = con.recv(1024)
    # dec = decrypt_message(recieved_msg.decode(), q, f, g)
    # print("Client message: ", dec)
