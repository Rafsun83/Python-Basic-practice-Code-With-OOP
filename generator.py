def genrator():
    yield 5
    yield 4
    yield 3

g = genrator()

# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

print(sorted(g))