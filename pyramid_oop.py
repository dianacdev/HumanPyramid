import time

rows = int(input("Enter number of rows: "))
t1_start = time.perf_counter()


cache = {}
# is caching the row,col as a tuple key and weight as the value

class Person():
    def __init__(self, row, col, weight, shoulder) -> None:
        self.row = row
        self.col = col
        self.weight = weight
        self.shoulder = shoulder

def weight_memo(row, col, weight):
    weight_memo.cache_hits += 1
    if ((row, col)) in cache:
        return cache[(row, col)]
    else:
        cache[(row, col)] = weight_on(row, col, weight)
        return cache[(row, col)]


def weight_on(row, col, weight):
    weight_on.calls += 1
    if row == 0:
        return 0
    elif col == 0:
        return (weight_memo(row-1, col, weight)+weight) / 2
    elif row == col:
        return (weight_memo(row-1, col-1, weight) + weight) / 2
    else:
        return weight + (weight_memo(row-1, col-1, weight)/2) + (weight_memo(row-1, col, weight)/2)


weight_memo.cache_hits = 0
weight_on.calls = 0
for i in range(rows):
    for j in range(i+1):
        print(f'{weight_on(i,j,200):.2f}', end=" ")
    print("")
t1_stop = time.perf_counter()
print(f"\nElapsed time: {t1_stop-t1_start} seconds")
print(f"Number of function calls: {weight_on.calls}")
print(f"Number of cache hits: {weight_memo.cache_hits}")
