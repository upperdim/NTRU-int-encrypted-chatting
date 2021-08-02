import socket
import pickle
from ntru import *

HEADERSIZE = 10

q = 122430513841
f = 231231
g = 195698

print('Waiting for server connection...')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1243))
print('Connected.')

while True:
    print("Wating for reply...")
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if (len(full_msg) - HEADERSIZE == msglen):
            enc = pickle.loads(full_msg[HEADERSIZE:])
            dec = decrypt_message(enc, q, f, g)
            print(dec)
            break 

    msg = input("Send message to server: ")
    enc = encrypt_message(msg, q, f, g)
    sendthis = pickle.dumps(enc)
    sendthis = bytes(f"{len(sendthis):<{HEADERSIZE}}", 'utf-8')+sendthis
    s.send(sendthis)
