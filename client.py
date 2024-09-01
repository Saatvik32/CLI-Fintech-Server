import socket
from sha import sha256
from datetime import datetime
import os
import re
import pandas as pd
from termcolor import colored
import time
import pyotp
import pyqrcode
from PIL import Image
from lsfr import generateID
from secret import generateSecret
from aes import encrypt as aes_encryption ,decrypt as aes_decryption
import base64

def sendmsg(message, s, addr):
    s.sendto(message.encode('utf-8'),addr)
    # username ,addr =s.recvfrom(1024) 

def rcv(data, addr, s):
    data,addr = s.recvfrom(1024)
    data=data.decode('utf-8')
    return data

def isNumber(txt,_min=6, _max=10): return True if re.match('^[0-9]{' + str(_min) + ',' + str(_max) + '}$',txt) else False
def isNotNumber(txt,_min=6, _max=10): return True if re.match('^[^0-9]{'+ str(_min) + ',' + str(_max) + '}$',txt) else False
def isEmail(txt): return True if re.match('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+',txt) else False
def isPassword(txt,_min=8, _max=12): return True if re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{' + str(_min) + ',' + str(_max)+'}$',txt) else False

def fetchSalt(file_name, username):
    result = []

    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if username in line:
                result.append((line.rstrip()))
                break

    if not result:
        return 0

    result = result[0].split()
    
    return result[-3]

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the host and port
host = '192.168.178.210'
# host = '127.0.0.1'
port = 3000

# client_socket.bind((host,port))
# Send data to the server
message = "Client has been connected"
client_socket.sendto(message.encode('utf-8'),(host,port))

def opt2(salt):
    username = input('Input Username : ')
    while not isNotNumber(username,8,10):
        print('Username Invalid')
        print('Username Must Contain 8-10 Character with No Number')
        username = input('Input Username : ')    
            
    passwd = input('Input Password : ')
    while not isPassword(passwd):
        print('Password Invalid')
        print('Password Must Contain 1 Uppercase, 1 Special Character, 1 Number and At Least 8 Character')
        passwd = input('Input Password : ')

    email = input('Input Email : ')
    while not isEmail(email):
        print('Email Invalid. example : john@gmail.com')
        email = input('Input Email : ')

    pin = input('Input PIN : ')
    while not isNumber(pin,6,6):
        print('PIN Invalid. PIN Must be Exactly 6 digits with no Alphabet')
        pin = input('Input PIN : ')

    phone = input('Input Phone Number : ')
    while not isNumber(phone,10,13):
        print('Phone Number Invalid. ex: 081234567892')
        phone = input('Input Phone Number : ')

    message =  str(username) + ' ' + sha256(passwd+salt) + ' ' + str(email) + ' ' + str(pin) + ' ' + str(phone)
    return message


# print("sent")
# Receive a response from the server
while True:
    data,addr = client_socket.recvfrom(1024)
    data=data.decode('utf-8')
    print(data)
    opt = input('>>> ')
    while opt not in ['1','2','0']:
        opt = input('Choose 1 / 2 / 0\n>>>')
    client_socket.sendto(opt.encode('utf-8'),addr)
    print(opt)
    if opt == '1':
        # data,addr = client_socket.recvfrom(1024)
        # data=data.decode('utf-8')
        # print(data)
        usr = input('Enter Username >>> ')
        client_socket.sendto(usr.encode('utf-8'),addr)
        data = rcv(data,addr,client_socket)
        if data == '1':
            # data=rcv(data,addr,client_socket)
            # print(data)
            passwd = input("Enter password >>")
            sendmsg(passwd,client_socket,addr)
            data = rcv(data,addr,client_socket)
            print(data)
            if data == '1':
                data=rcv(data,addr,client_socket)
                print(data)
                if data == '1':
                    while True:
                        data=rcv(data,addr,client_socket)
                        print(data)
                        data=rcv(data,addr,client_socket)
                        print(data)
                        opt0 = input('>>> ')
                        while opt0 not in ['1','2','3','4','5','0']:
                            data=rcv(data,addr,client_socket)
                            opt0 = input('Choose 1 / 2 / 3 / 4 / 5 / 0\n>>> ')
                        sendmsg(opt0,client_socket,addr)
                        
                        if opt0 == '1':
                            bank = input('Input Bank : ')
                            while not isNotNumber(bank,3,10):
                                print('Bank Must Contain 3-10 Character with No Number')
                                bank = input('Input Bank : ')
                            sendmsg(bank,client_socket,addr)

                            amount = input('Input Amount of Money : ')
                            while not isNumber(amount,5,8):
                                print('Amount Invalid. Amount Must Not Have Alphabet')
                                amount = input('Input Amount : ')

                            sendmsg(amount,client_socket,addr)  
                            data=rcv(data,addr,client_socket)
                            print(data)                      
                        
                        if opt0 == '2':
                            print("transfer")
                            data=rcv(data,addr,client_socket)
                            print(data)
                            pt0 = input('>>> ')
                            while pt0 not in ['1','0']:
                                pt0 = input('Enter 0 or 1\n>>> ')
                            sendmsg(pt0,client_socket,addr)
                            if (pt0 == '1'):
                                ibtm = False

                                while True:
                                    data= rcv(data,addr,client_socket)
                                    print(data)
                                    phone = input('>>> ')
                                    while not isNumber(phone,10,13):
                                        print('Phone Number Not Valid. ex: 081234567892')
                                        phone = input('Input Phone Number : ')
                                    sendmsg(phone,client_socket,addr)
                                    data = rcv(data,addr,client_socket)
                                    if data == '1':
                                        data = rcv(data,addr,client_socket)
                                        print('Receiver : ', data)
                                        break
                                    elif data == '300':
                                        data = rcv(data,addr,client_socket)
                                        print(data)
                                    elif data == '400':
                                        data = rcv(data,addr,client_socket)
                                        print(data)

                                amount = input("Input amount: ")
                                while not isNumber(amount,5,8):
                                    print('Amount Invalid. Amount Must Not Have Alphabet')
                                    amount = input('Input Amount : ')

                                data = rcv(data,addr,client_socket)
                                money = data
                                print("Money left : " + money)

                                while int(money) - int(amount) < 0:
                                    print('You Don\'t Have Enough Money to Transfer Rp.',amount)
                                    chc = input('Go Back (0) | Continue (1)\n>>> ')

                                    while chc not in ['0','1']:
                                        chc = input('Choose 1 / 0\n>>> ')
                                                
                                        if chc == '0':
                                            ibtm = True
                                            sendmsg('1',client_socket,addr)
                                            break
                                        else:
                                            # sendmsg('1',client_socket,addr)
                                            amount = input('Input Amount : ')
                                            while not isNumber(amount,5,8):
                                                print('Amount Invalid. Amount Must Not Have Alphabet')
                                                amount = input('Input Amount : ')

                                sendmsg('0',client_socket,addr)
                                desc = 's'
                                pin ='d'
                                if not ibtm :
                                    desc = input('Input Description : ')
                                    while len(desc) > 20:
                                        print('Maximum Description Length Must Be 20 Characters')
                                        desc = input('Input Description : ')

                                    pin = input('Enter PIN : ')
                                    while not isNumber(pin,6,6):
                                        print('PIN Invalid. PIN Must be Exactly 6 digits with no Alphabet')
                                        pin = input('Input PIN : ')
                                    
                                    sendmsg(pin,client_socket,addr)
                                    sendmsg(desc,client_socket,addr)
                                else: 
                                    continue
                                data = rcv(data,addr,client_socket)
                                print(data)
                            else: continue

                        elif opt0 == '3':
                            print('history')
                            data = rcv(data,addr,client_socket)
                            print(data)
                            print('\n\n\n')
                            print('==================================')

                        elif opt0 == '4':
                            print('Download history')
                            chc = input('Download to Excel (0) | Download to CSV (1)\n>>> ')
                            while chc not in ['0','1']:
                                chc = input('Choose 1 / 0\n>>> ')

                            sendmsg(chc,client_socket,addr)
                            if chc == '1':
                                data, _ = client_socket.recvfrom(4096)
                                with open('receipt.xlsx', 'wb') as file:
                                    file.write(data)
    
                            else:
                                data, _ = client_socket.recvfrom(4096)
                                with open('receipt.csv', 'wb') as file:
                                    file.write(data)
                            print("File received")
                        elif  opt0 == '5':
                            print('security')
                            chc = input('Go Back (0) | Continue (1)\n>>> ')
                            sendmsg(chc,client_socket,addr)
                            if chc == '1':
                                ch = input('Deactivate (0) | Activate (1)\n>>> ')
                                sendmsg(ch,client_socket,addr)
                                if ch == '0':
                                    data=rcv(data,addr,client_socket)
                                    print(data)
                                elif ch == '1':
                                    data, _ = client_socket.recvfrom(4096)
                                    with open('Auth.png', 'wb') as file:
                                        file.write(data)
                                    print("Image received")
                                    # url.png('myqr.png', scale = 6)
                                    img = Image.open('Auth.png')
                                    img.show()
                                    time.sleep(1)
            
                                    os.remove("Auth.png")


                        if opt0 == '0':
                            print("Application closed Successfully")
                            quit()
                    # elif opt0 == '2':
                else:
                    print('Login Error!!')
            else:
                print('Login Error, Wrong password!!')
        else:
            print("User doesn't exist")


    elif (opt=='2'):
        data=rcv(data,addr,client_socket)
        opt=opt2(data)
        client_socket.sendto(opt.encode('utf-8'),addr)
        data,addr = client_socket.recvfrom(1024)
        data=data.decode('utf-8')
        print(data)
    elif (opt=='0'):
        data,addr = client_socket.recvfrom(1024)
        data=data.decode('utf-8')
        print(data)
        break

    else:
        continue


# print("Logged Out Successfully")
# Close the connection
client_socket.close()
