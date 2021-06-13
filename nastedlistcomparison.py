matrix = [
    [1,2,3,4],
    [2,3,5,1],
    [4,2,5,7],
]
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)


result = list(zip(*matrix))
print(result)
