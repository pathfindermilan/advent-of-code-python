import re
from collections import Counter

data = open('input.txt').read().strip()
l = data.split("\n")

def extract(l, p):
    winning_side, my_side = l.split(':')[1].split('|')
    w = re.findall(p, winning_side)
    m = re.findall(p, my_side)
    winning_array = [i for i in map(int, w)]
    my_numbers = [i for i in map(int, m)]

    return winning_array, my_numbers

# part 1

p = r'\d{1,2}'
ans = 0
for ll in l:
    winning_array, my_numbers = extract(ll, p)

    guesses = 0
    for i in range(len(winning_array)):
        if winning_array[i] in my_numbers:
            guesses += 1
    if guesses:
        ans += pow(2, guesses-1)
print(ans)

# part 2

helper = Counter()

for ll_index, ll in enumerate(l):
    winning_array, my_numbers = extract(ll, p)

    guesses = 0
    for i in range(len(winning_array)):
        if winning_array[i] in my_numbers:
            guesses += 1
    helper[ll_index] += 1

    for i in range(ll_index, ll_index + guesses):
        if i+1 < len(l):
            helper[i+1] += helper[ll_index]
        else: break

ans = sum(helper.values())
print(ans)

