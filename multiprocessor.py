from multiprocessing import Process, Value, Array,Lock
import time
from threading import Thread


def add_100(number, lock):
    for i in range(100):
        with lock:
          time.sleep(0.001)
          number.value +=1




if __name__ == "__main__":

    shared_number = Value('i',0)
    lock = Lock()
    print("started value is:  ", shared_number.value)

    p1 = Process(target=add_100, args= (shared_number,lock))
    p2 = Process(target=add_100, args= (shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("end value is : ", shared_number.value)

