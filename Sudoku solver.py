def check(lst):
    required= set(range(1, 9))
    input_set = set(lst)
    missing_numbers = required - input_set
    if missing_numbers:
        return missing_numbers
    else:
       return 1





#initialises the grid and its structure
rows, columns = 3, 3
grid = []

#takes input of the box
for r in range(rows):
    number=input().strip()
    if number.isdigit():
        row = list(map(int, list(number)))  # Convert each character to an integer
    else:
        # If the input is space-separated (like "1 3"), split by spaces and convert to integers
        row = list(map(int, number.split()))
    grid.append(row)

flattened_grid = [num for row in grid for num in row]
result = check(flattened_grid)
print (flattened_grid)
print(result)


#for x in range(rows):
 #  for y in range(columns):
  #     compare = grid[x][y]
   #    print(compare)
#
 #      for x1 in range(rows):
  #         for y1 in range(columns):
   #           current= grid [x1][y1]
    #          print(current)
