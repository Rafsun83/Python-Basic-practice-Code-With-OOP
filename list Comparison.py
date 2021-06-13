

# result = [(x, y) for x in [1,2,3] for y in [2, 3,5] if x!=y]
# print(result)

value = []

for x in [1,3,6]:
    for y in [2,5,8]:
        if x!=y:
            value.append((x, y))


print(value)