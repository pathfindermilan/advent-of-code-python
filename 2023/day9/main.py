import re

data = open('input.txt').read().strip()
l = data.split("\n")

p = r'-?\d+'
ans1 = 0
ans2 = 0
for ll in l:
    all_arr = []
    values = list(map(int, re.findall(p, ll)))
    all_arr.append(values)
    while not all(v == 0 for v in all_arr[-1]):
        new_sequence = [all_arr[-1][i + 1] - all_arr[-1][i] for i in range(len(all_arr[-1]) - 1)]
        all_arr.append(new_sequence)
    # part 1
    next_value = sum(seq[-1] for seq in all_arr[::-1])
    ans1 += next_value

    # part 2
    ans2 += sum(pre[0] - nex[0] for pre, nex in zip(all_arr[::2], all_arr[1::2]))

print(ans1)
print(ans2)
