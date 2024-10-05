arr = [[0 for _ in range(7)] for _ in range(7)]

for i in range(7):
    for j in range(7):
        if j % 2 == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for row in arr:
    print(row)
