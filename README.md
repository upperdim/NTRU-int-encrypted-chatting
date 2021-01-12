NTRU Integer encrypted chatting over socket. 

Program is inside `4_doesnt_work_combined` folder

```
 1. Program inputs a string
 2. Calls encrypt_message() to encrypt the string before sending
 3.     encrypt_message()
 4.     Iterates over each character in the string
 5.         Converts that character to integer
 6.         Encrypts that integer with NTRU algorithm
 7.         Appends encrypted integer into an int array
 8.     returns the int array obtained by encrypting each character in the string
 9. Program sends the int array to the opposite side over a socket
10. 
11. Opposite side recieves the array
12. Decrypts the int array to a string
13. Prints the array
14. Does the same things as Step 1, they communicate back and forth 1 by 1

```

Sources:

3_sending_array: https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
