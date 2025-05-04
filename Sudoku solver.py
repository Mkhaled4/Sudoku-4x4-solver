def check(lst):
    required= set(range(1, 10))
    input_set = set(lst)
    missing_numbers = required - input_set
    if missing_numbers:
        return missing_numbers
    else:
       return True





#initialises the grid and its structure
rows, columns = 2,9
grid = []

#takes input of the box
for r in range(rows):
    number=input()
    new= number.replace(" ","0")
    print(new)
    row = list(map(int, list(new)))

    grid.append(row)

print(grid)

for row in grid:
    result=check(row)
    print(result)

for columns in grid:
    result=check(columns)
    print(result)
