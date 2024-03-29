from math import floor, gcd, sqrt
from random import randint
from sys import exit


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


def error_exit(err_msg):
	"""Exits the program by printing the err_msg to console first"""
	print(err_msg)
	exit()


def ntru_encrypt(m, q, f, g):
	# key creation
	if f >= sqrt(q/2):
		error_exit("error: ntru_encrypt(): f out of range")
	if sqrt(q/4) >= g or g >= sqrt(q/2):
		error_exit("error: ntru_encrypt(): g out of range")
	if gcd(f, g*q) != 1:
		error_exit("error: ntru_encrypt(): gcd condition failed")
	if m >= sqrt(q/4):
		error_exit("error: ntru_encrypt(): m out of range")

	h = (modinv(f, q) * g) % q

	priv_key = [f, g]
	pub_key  = [q, h]

	# encryption
	r = randint(1, floor(sqrt(q/2)))
	if r >= sqrt(q/2):
		error_exit("error: ntru_encrypt(): r out of range")

	e = (r * h + m) % q
	return e 


def ntru_decrypt(e, q, f, g):
	a = (f * e) % q
	if 0 > a or a > q:
		error_exit("error: ntru_decrypt(): a out of range")

	b = (modinv(f, g) * a) % g
	if 0 > b or b > g:
		error_exit("error: ntru_decrypt(): b out of range")

	return b


def encrypt_message(msg, q, f, g):
	"""receives msg  (string)
	   returns 'new' (integer array)"""
	new = []

	for element in msg:
		# convert that element to int
		conv = ord(element) 
		
		# call the func with converted int
		enc = ntru_encrypt(conv, q, f, g)

		# add it to our int array that we will send
		new.append(enc)
		
	return new


def decrypt_message(enc, q, f, g):
	"""receives enc  (integer)
	   returns 'new' (string)"""
	new = ""
	for element in enc:
		character = chr( ntru_decrypt(element, q, f, g) )  # append decrypted char
		new += character
	return new	


# driver code for testing ntru_encrypt() ntru_decrypt()

# q = 122430513841
# f = 231231
# g = 195698

# msg = 123456
# en = ntru_encrypt(msg, q, f, g)
# print("en : ", en) # debug

# dec = ntru_decrypt(en, q, f, g)
# print("dec : ", dec) # debug

# if (msg == dec):
# 	print("=========================")
# 	print("=                       =")
# 	print("=        SUCCESS        =")
# 	print("=                       =")
# 	print("=========================")
# else:
# 	print("<<<<<<<< FAIL >>>>>>>>")
