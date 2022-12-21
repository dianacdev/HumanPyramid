import time

rows = int(input("Enter number of rows: "))
t1_start = time.perf_counter()


def weight_on(row, col, weight):
    weight_on.calls += 1
    if row == 0:
        return 0
    elif col == 0:
        return (weight_on(row-1, col, weight)+weight) / 2
    elif row == col:
        return (weight_on(row-1, col-1, weight) + weight) / 2
    else:
        return weight + (weight_on(row-1, col-1, weight)/2) + (weight_on(row-1, col, weight)/2)

output_file = open("part 2.out","w")
weight_on.calls = 0
for i in range(rows):
    for j in range(i+1):
        str1 = (f'{weight_on(i,j,200):.2f}  ')
        output_file.write(str1)
    str2 =(f"\n")
    output_file.write(str2)
t1_stop = time.perf_counter()
str= (f"\nElapsed time: {t1_stop-t1_start} seconds\nNumber of function calls: {weight_on.calls}")
output_file.write(str)
output_file.close()
# print(f"\nElapsed time: {t1_stop-t1_start} seconds")
# print(f"Number of function calls: {weight_on.calls}")
