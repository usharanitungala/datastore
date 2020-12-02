import threading
from threading import*
import time
import backendcode as x
x.create("sastra",25)

x.create("main",70,3800)

x.read("sastra")

x.read("main")

x.create("sastra",150)

x.modify("sastra",550)

x.delete("sastra")

key_name = input()
value = int(input())
timeout = int(input())
t1=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t1.start()
t1.join()
key_name = input()
value = int(input())
timeout = int(input())
t2=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t2.start()
t2.join()