#initialises the grid and its structure
rows, columns = 3, 3
grid = []

#takes input of the box
for r in range(rows):
    number=input()
    row = list(map(int,number))
    grid.append(row)


x,y=2,0


for row in grid:
    compare = grid[x][y]
    for n in row:
       if n == compare:
           print("yes")
       else:
           print("no")
    print(row)
    y += 1
    print (y)
    print(compare)
    print (x)

