row: str=input("Enter the row of matrix:")
row_=int(row)
column:int=input("Enter the column of matrix")
column_=int(column)
matrix=[]
_row=[]
for i in range(0,row_):
    for j in range(0,column_):
        _row.append(i*j)
    matrix.append(_row)

print(matrix)