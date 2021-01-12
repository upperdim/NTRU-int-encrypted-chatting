import socket
import pickle
from ntru import *

HEADERSIZE = 10

q = 122430513841
f = 231231
g = 195698

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1243))

while True:
    print("Wating for reply...")
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        
        print(f"full message length : {msglen}")

        full_msg += msg

        if (len(fullmsg - HEADERSIZE == msglen)):
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""

    # recieved_msg = s.recv(1024)
    # dec = decrypt_message(recieved_msg.decode(), q, f, g)
    # print("message from server: ", dec)

    msg = input("send message to server: ")
    enc = encrypt_message(msg, q, f, g)
    s.send(enc.encode())