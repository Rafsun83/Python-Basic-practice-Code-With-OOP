def fibonacci(n):
    a , b = 0 ,1
    while a<n:
        yield a
        a , b = b , a+b

value = fibonacci(30)
for x in value:
    print(x)
