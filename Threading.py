from threading import Thread
def one():
    for x in range (100):
        print("one")
def two():
    for x in range(100):
        print("two")

t1 = Thread(target=one)
t2 = Thread(target=two)

t1.start()
t2.start()
t1.join()