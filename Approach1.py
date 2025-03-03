
# This implements two thread synchronized with eachother to process tasks.

from threading import Thread

global flag 
flag = 0

def func1():
    global flag
    for i in range(1, 10, 2):
        while flag != 0:
            continue
        print(i)
        flag = 1
    
def func2():
    global flag
    for i in range(2, 10, 2):
        while flag != 1:
            continue
        print(i)
        flag = 0

thrd1 = Thread(target=func1)
thrd2 = Thread(target=func2)

thrd1.start()
thrd2.start()
