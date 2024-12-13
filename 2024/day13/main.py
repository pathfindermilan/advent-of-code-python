import re
import numpy as np

data = open('input.txt').read().strip().split('\n\n')
p = r"\d+"

c = lambda a, b, m, n, x, y: (np.divide((x * n - y * m), (a * n - b * m)), np.divide((x - a * np.divide((x * n - y * m), (a * n - b * m))), m))
ch = lambda i_j, part: all(isinstance(val, int) or val.is_integer() for val in i_j) and (all(0 <= val <= 100 for val in i_j) if part == 1 else True)
ans1 = sum(int(i * 3 + j) for ll in data for i, j in [c(*map(int, re.findall(p, ll)))] if ch((i, j), 1))
ans2 = sum(int(i * 3 + j) for ll in data for i, j in [c(*map(int, re.findall(p, ll)[:4]), *map(lambda x: int(x) + 10000000000000, re.findall(p, ll)[4:]))] if ch((i, j), 2))

print(ans1, ans2)