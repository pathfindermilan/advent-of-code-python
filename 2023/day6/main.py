from functools import reduce
import re

p = r"\d+"
t, d = open('input.txt').read().strip().split("\n")
tt, dd= list(map(int, re.findall(p, t))), list(map(int, re.findall(p, d)))

def counts(t, d):
    for i in range(1, t // 2 + 1):
        if i * (t - i) > d:
            break
    return (t - 1) - 2 * (i - 1)

# part 1
def product(times, distances):
    return reduce(lambda x, y: x * y, (counts(t, d) for t, d in zip(times, distances)))

ans = product(tt, dd)
print(ans)

# part 2
ttt = "".join(str(t) for t in tt)
ddd = "".join(str(d) for d in dd)
ttt = int(ttt)
ddd = int(ddd)

count = counts(ttt, ddd)
print(count)