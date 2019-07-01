
arr1 = ['hello', 'python', 'technology','science']
result = []
for w in arr1:
    print(w.upper())
    tatList = []
    for ch in w:
        tatList.append(ch)
    result.append(tatList)

print(result)

matrix = [[5, 5, 5], [1, -9, 44, 7], [-20, 10, 5]]

result = []
for tatReshima in matrix:
    result.append(sum(tatReshima))
print(result)
print(min(result))
print(result.index(min(result)))






