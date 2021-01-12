import math
import random
import sys

# they all work - driver code at the bottom

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def ntru_encrypt(m, q, f, g):
	# key creation
	if ( f >= math.sqrt(q/2) ):
		print("error: ntru_encrypt(): f out of range")
		sys.exit()
	if ( math.sqrt(q/4) >= g or g >= math.sqrt(q/2) ):
		print("error: ntru_encrypt(): g out of range")
		sys.exit()
	if ( math.gcd(f, g*q) != 1 ):
		print("error: ntru_encrypt(): gcd condition failed")
		sys.exit()
	if ( m >= math.sqrt(q/4) ):
		print("error: ntru_encrypt(): m out of range")
		sys.exit()

	h = ( modinv(f, q) * g ) % q
	#print("h : ", h) # debug

	priv_key = [f, g]
	pub_key = [q, h]

	# encryption
	r = random.randint(1, math.floor(math.sqrt(q/2)))
	#r = 113500 # debug # careful
	if ( r >= math.sqrt(q/2) ):
		print("error: ntru_encrypt(): r out of range")
		sys.exit()

	e = (r * h + m) % q
	return e 

def ntru_decrypt(e, q, f, g):
	a = (f * e) % q
	#print("a : ", a) # debug
	if ( 0 > a or a > q):
		print("error: ntru_decrypt(): a out of range")
		sys.exit()

	b = (modinv(f, g) * a) % g
	#print("b : ", b) # debug
	if ( 0 > b or b > g):
		print("error: ntru_decrypt(): b out of range")
		sys.exit()

	return b


# driver code for testing ntru_encrypt() ntru_decrypt()
# all works

q = 122430513841
f = 231231
g = 195698

msg = 123456
en = ntru_encrypt(msg, q, f, g)
print("en : ", en) # debug

dec = ntru_decrypt(en, q, f, g)
print("dec : ", dec) # debug

if (msg == dec):
	print("=========================")
	print("=                       =")
	print("=        SUCCESS        =")
	print("=                       =")
	print("=========================")
else:
	print("<<<<<<<< FAIL >>>>>>>>")
