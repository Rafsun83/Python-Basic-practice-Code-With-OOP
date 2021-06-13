

def count(num):
    while num>0:
      yield num
      num-=1


number = count(5)



# for x in number:
#     print(x)
try:
  value = next(number)
  print(value)

  print(next(number))
  print(next(number))
  print(next(number))
  print(next(number))
  print(next(number))
except StopIteration:
    print("this is value error")