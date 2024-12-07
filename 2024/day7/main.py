import re

data = open('input.txt').read().strip()
l = data.split("\n")

p = r'\d+'
ans = 0

def ok(t, a):
    p = {a[0]}
    for c in a[1:]:
        p = {
            clc(pr, c)
            for pr in p
            for clc in [
                lambda x, y: x + y,
                lambda x, y: x * y,
                lambda x, y: int(str(x) + str(y))  # part 2
            ]
        }
    return t in p

for ll in l:
    left, right = ll.split(":")
    goal = int(left)
    values = list(map(int, re.findall(p, right)))
    if ok(goal, values):
        ans+=goal
print(ans)