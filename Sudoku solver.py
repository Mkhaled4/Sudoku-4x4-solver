#initialises the grid and its structure
rows, columns = 3, 3
grid = []

#takes input of the box
for r in range(rows):
    number=input()
    row = list(number)
    grid.append(row)




for x in range(rows):
   for y in range(columns):
       compare = grid[x][y]
       print(compare)

       for x1 in range(rows):
           for y1 in range(columns):
              current= grid [x1][y1]
              print(current)
