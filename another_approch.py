global lock
lock = True

def even():
    global lock
    for i in range(0, 30, 2):
        #print("even", lock, i)
        while True:
            if lock:
                #print("\ncoming-->", i)
                print("In Even Block --> ",i)
                lock = False
                break
            else:
                continue

def odd():
    global lock
    for i in range(1, 30, 2):
        #print("odd", lock, i)
        while True:
            if not lock:
                #print("\ncoming-->", i)
                print("In Odd Block --> ",i)
                lock = True
                break
            else:
                continue

from threading import Thread
#import threading

Thread(target=even).start()
Thread(target=odd).start()
