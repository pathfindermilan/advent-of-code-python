import re
from collections import defaultdict
from itertools import product, combinations

data = open('input.txt').read().strip()
l = data.split("\n")

dict_symbols = defaultdict(list)
_ = list(map(lambda rc: dict_symbols[l[rc[0]][rc[1]]].append(rc)
             if l[rc[0]][rc[1]] != '.' else None,
             product(range(len(l)), range(len(l)))))
# part 1
a1 = set()
a2 = set()
for cor in dict_symbols.values():
    for (row1, col1), (row2, col2) in combinations(cor, 2):
        for x, y in [(row1 + (row1-row2), col1 + (col1-col2)), (row2 + (row2-row1), col2 + (col2-col1))]:
            if x in range(len(l)) and y in range(len(l[0])):
                a1.add((x, y))
        # part 2
        for d in [1, -1]:
            x, y = row1, col1
            while x in range(len(l)) and y in range(len(l[0])):
                a2.add((x, y))
                x += d * (row2 - row1)
                y += d * (col2 - col1)
print(len(a1))
print(len(a2))