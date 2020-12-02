import threading 
from threading import*
import time

d={}

def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message 1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:  #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ") #error message 2
        else:
            print("error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers") #error message 3

def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message 4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message 5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message 4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message 5
        else:
            del d[key]
            print("key is successfully deleted")

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message 6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message 5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message 6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l