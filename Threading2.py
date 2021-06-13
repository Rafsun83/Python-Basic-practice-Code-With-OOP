from threading import Thread,Lock
import time

databasevalue = 0


def thread(lock):


    global databasevalue

    with lock:

    # lock.acquire()
        localcopy = databasevalue
        localcopy +=1
        time.sleep(0.1)
        databasevalue = localcopy
    # lock.release()

if __name__ == "__main__":

    lock = Lock()
    print("start ", databasevalue)

    t1 = Thread(target=thread(lock))
    t2 = Thread(target=thread(lock))

    t1.start()
    t2.start()

    print("end ", databasevalue)
    print("end main")

