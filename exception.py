list = [ 12, 3,4 ,23, 4, 0]

try:
    result = list[2]/ list[5]
    print(result)

except ZeroDivisionError:
    print("this is zero division error")

