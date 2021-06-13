import sys
def generate(n):
    nums = []
    num = 0
    while num <n:
        nums.append(num)
        num +=1
    return nums


value = generate(1000000)
print(sys.getsizeof(value))


def G_generate(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sys.getsizeof(G_generate(1000000)))
