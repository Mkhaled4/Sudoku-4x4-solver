# solves the case where only one number is missing from the row/column
def solv1(lst):

    required = set(range(1, 5))
    input_set = set(lst)
    missing_numbers = required - input_set
    update_miss=list(missing_numbers)
    final_lst = [update_miss[0] if x == 0 else x for x in lst]
    return final_lst

#solves the row where two numbers are missing from the row/column by then checking the corresponding column/row
def solv2(lst, lst2):
        required = set(range(1, 5))
        input_set = set(lst)
        missing_numbers = required - input_set
        update_miss = list(missing_numbers)

        i = 0
        for x in range(len(lst)):
            if lst[x] == 0:
                while i < len(update_miss) and update_miss[i] in lst2:
                    i += 1
                if i < len(update_miss):
                    lst[x] = update_miss[i]
                    i += 1
        return lst

#takes in the grid and column 2D arrays and solves it using recursion
def answer(grid1, column1):
    grid_1d = [element for sublist in grid1 for element in sublist]
    column_1d = [element for sublist in column1 for element in sublist]
    num_count = sum(grid_1d.count(i) for i in range(1, 5))

# checks if the grid is complete or not
    if 0 not in grid_1d and 0 not in column_1d:
        return grid1,column1
#checks if the grid is possible or not where it is impossible if there are less than 4 values
    elif num_count < 4:
        return "impossible", "impossible"
    else:

        for x in range(len(grid1)):
            for y in range(len(grid1[0])):

                x_val = []
                y_val = []
                #checks the grid's zero count
                if grid1[x][y] == 0 and grid1[x].count(0) == 1:
                    x_val.append(x)
                    y_val.append(y)
                    grid1[x] = solv1(grid1[x])
                    column1[y_val[0]][x_val[0]] = grid1[x_val[0]][y_val[0]]   #replaces the corresponding column value with the grid's value
                    return answer(grid1, column1)

                elif column1[x][y] == 0 and column1[x].count(0) == 1:
                    x_val.append(x)
                    y_val.append(y)
                    column1[x] = solv1(column1[x])
                    grid1[y_val[0]][x_val[0]] = column1[x_val[0]][y_val[0]]
                    return answer(grid1, column1)
                # checks the grid's count for more than one zero
                elif grid1[x][y] == 0 and grid1[x].count(0) == 2:
                    x_val.append(x)
                    y_val.append(y)
                    grid1[x] = solv2(grid1[x],column1[y])
                    column1[y_val[0]][x_val[0]] = grid1[x_val[0]][y_val[0]]
                    return answer(grid1, column1)

                elif column1[x][y] == 0 and column1[x].count(0) == 1:
                    x_val.append(x)
                    y_val.append(y)
                    column1[x] = solv2(column1[x],grid1[y])
                    grid1[y_val[0]][x_val[0]] = column1[x_val[0]][y_val[0]]
                    return answer(grid1, column1)








rows, columns = 4,4
grid = []

#takes in the sudoku numbers and changes any space into a zero
for r in range(rows):
    number=input()
    new= number.replace(" ","0")
    row = list(map(int, list(new)))

    grid.append(row)

#flips the 2d array into columns rather than rows
column = []
for col_index in range(4):
    indcol=[]
    for row_index in range(4):
        indcol.append(grid[row_index][col_index])
    column.append(indcol)

#prints the final grid row by row
f_grid,f_column = answer(grid,column)
for x in f_grid:
    print(x,"\n")


