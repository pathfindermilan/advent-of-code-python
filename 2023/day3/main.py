import re
from collections import Counter

data = open('input.txt').read().strip()
l = data.split("\n")

p = r'\d+'
def check_for_symbol_cases(k, v, length):
    return [
        (key[0], key[1]-1),
        (key[0], key[1]+len_num),
        *[(key[0]-1, c) for c in range(key[1]-1, key[1]+len_num+1)],
        *[(key[0]+1, c) for c in range(key[1]-1, key[1]+len_num+1)],
    ]

# part 1
ans = 0
d = dict()
all_symbols = ['#', '+', '@', '%', '&', '/', '-', '=', '*', '$']

for ll_index, ll in enumerate(l):
    numbers = re.finditer(p, ll)
    for n in numbers:
        d[(ll_index, n.start())] = int(n.group())

for key, value in d.items():
    len_num = len(str(value))
    check_for_symbol = check_for_symbol_cases(key, value, len_num)

    for i, j in check_for_symbol:
        try:
            maybe_symbol = l[i][j]
            if maybe_symbol in all_symbols:
                ans += int(value)
                break
        except: continue
print(ans)


# part 2
ans = 0
products = dict()
all_symbols = ['*']

for key, value in d.items():
    len_num = len(str(value))
    check_for_symbol = check_for_symbol_cases(key, value, len_num)

    for i, j in check_for_symbol:
        try:
            maybe_symbol = l[i][j]
            if maybe_symbol in all_symbols:
                if (i, j) not in products:
                    products[(i, j)] = [int(value), 1]
                else:
                    products[(i, j)][0] *= int(value)
                    products[(i, j)][1] += 1
        except: continue

for product in products.values():
    if product[1] == 2: ans += product[0]

print(ans)