# ntru-int-encrypted-chatting
NTRU Integer encrypted chatting over socket. 

Program is inside `4_doesnt_work_combined` folder

```
Program inputs a string

Calls encrypt_message() to encrypt the string before sending

    encrypt_message()
    
    Iterates over each character in the string
    
        Converts that character to integer
        
        Encrypts that integer with NTRU algorithm
        
        Appends encrypted integer into an int array
        
    returns the int array obtained by encrypting each character in the string
    
Program sends the int array to the opposite side over a socket <- problem


Opposite side recieves the array <- problem
```
