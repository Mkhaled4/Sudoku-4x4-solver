def check(lst):
    required= set(range(1, 5))
    input_set = set(lst)
    missing_numbers = required - input_set
    if missing_numbers:
        return missing_numbers
    else:
       return True

def solv1(lst):
    print(lst)
    required = set(range(1, 5))
    input_set = set(lst)
    missing_numbers = required - input_set
    print(missing_numbers)
    final_lst = [missing_numbers if x == 0 else x for x in lst]
    return final_lst

def solv2(lst):
    print(lst)
    required = set(range(1, 5))
    input_set = set(lst)
    missing_numbers = required - input_set
    print(missing_numbers)
    final_lst = [missing_numbers if x == 0 else x for x in lst]
    return final_lst



rows, columns = 4,4
grid = []


for r in range(rows):
    number=input()
    new= number.replace(" ","0")
    row = list(map(int, list(new)))

    grid.append(row)



for row in grid:
    result=check(row)



column = []
for col_index in range(4):
    indcol=[]
    for row_index in range(4):
        indcol.append(grid[row_index][col_index])
    column.append(indcol)

for row in column:
    result=check(row)


for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x].count(0) == 1:
           grid[x] = solv1(grid[x])

        if column[x].count(0) == 1:
           column[x] = solv1(column[x])

        if grid[x].count(0) == 2:
           grid[x] = solv2(grid[x])


print(column)


