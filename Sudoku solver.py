rows, columns = 3, 3
grid = []

for r in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

for row in grid:
    print(row)
