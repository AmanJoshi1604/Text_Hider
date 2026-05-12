import cv2
import os
import string

img = cv2.imread("jec.png")

msg = input("Enter Secert Message:")

password = input("Enter Password:")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

m=0
n=0
z=0

for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encrypted_Message.jpg",img)

os.system("Start Encrypted_Message.jpg")


message=""

n=0
m=0
z=0

pas = input("Enter Passcode For Decryption:")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decrypted Message:",message)
else:
    print("Not a Valid Key!!!")
