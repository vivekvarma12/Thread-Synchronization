from threading import Thread, Lock

flag = 0
lock = Lock()

def func1():
    global flag
    for i in range(1, 10, 2):
        while True:
            with lock:
                if flag == 0:
                    print(i)
                    flag = 1
                    break

def func2():
    global flag
    for i in range(2, 10, 2):
        while True:
            with lock:
                if flag == 1:
                    print(i)
                    flag = 0
                    break

thrd1 = Thread(target=func1)
thrd2 = Thread(target=func2)

thrd1.start()
thrd2.start()
