rows, columns = 3, 3
row = []
grid=[]
num=0
for r in range(rows):
    for c in range(columns):
        num += 1
        row.append(num)
    print(row)
    row=[]



