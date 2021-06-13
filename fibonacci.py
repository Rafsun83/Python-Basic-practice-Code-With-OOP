# a, b = 0, 1
# while a<10:
#     print(a, end=',')
#



#if statement
x = int(input("Please enter an integer: "))

if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')