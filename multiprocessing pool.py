from multiprocessing import Pool
import time


def cube(number):
    return  number*number*number




if __name__ == "__main__":
    number = range(10)

    pool = Pool()

    result = pool.map(cube, number)

    pool.close()
    pool.join()

    print(result)