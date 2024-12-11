from collections import defaultdict
import re

s = [int(ss) for ss in re.findall(r'\d+', open('input.txt').read().strip())]

def t(x):
    if x == 0: return tuple([1])
    y = str(x)
    return tuple([int(y[:len(y) // 2]), int(y[len(y) // 2:])]) if len(y) % 2 == 0 else tuple([x * 2024])

def steps(x, st):
    d = defaultdict(lambda: defaultdict(int))
    d[0].update({xx: 1 for xx in x})
    [[d[stt+1].__setitem__(xx, d[stt + 1][xx] + y) for x, y in d[stt].items() for xx in t(x)] for stt in range(st)]
    return sum(d[st].values())

# part 1
print(steps(s, 25))
# part 2
print(steps(s, 75))
