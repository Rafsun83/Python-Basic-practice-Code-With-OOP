# for item in [1, 2, 3, 4,]:
#     for x in ['a','b']:
#         print(item,x)

user = {
    'name': 'rafsun',
    'age': 23,
    'status': 'student'
}

for value in user.values():
    print(value)
for key in user.keys():
    print(key)
for x, y in user.items():
    print(x, y)