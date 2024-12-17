import copy
import re
from functools import reduce

p = r"\d+"
data = open('input.txt').read().strip()
regA, regB, regC, *program = map(int, re.findall(p, data))

combo = lambda o: o if 0 <= o <= 3 else (regA if o == 4 else (regB if o == 5 else (regC if o == 6 else None)))

# part 1
helper = 0
arr = list()
while helper < len(program):
    x, y = program[helper], program[helper + 1]
    if x == 0: regA >>= combo(y)
    elif x == 1: regB ^= y
    elif x == 2: regB = combo(y) % 8
    elif x == 3 and regA != 0: helper = y - 2
    elif x == 4: regB ^= regC
    elif x == 5: arr.append(combo(y) % 8)
    elif x == 6: regB = regA >> combo(y)
    elif x == 7: regC = regA >> combo(y)
    helper += 2
helper_string = "".join(f"{i}," for i in arr)[:-1]
print(helper_string)

# part 2
def helper_fn(program_, ans):
    helper_program = copy.deepcopy(program)
    if not program_: return ans
    for i in range(8):
        regA, regB, regC = ans << 3 | i, 0, 0
        combo = lambda o: o if 0 <= o <= 3 else (regA if o == 4 else (regB if o == 5 else (regC if o == 6 else None)))

        def kk(s, x_y):
            nonlocal regA, regB, regC
            x, y = x_y
            if x == 1: regB ^= y
            elif x == 2: regB = combo(y) % 8
            elif x == 4: regB ^= regC
            elif x == 5: s['output'] = combo(y) % 8
            elif x == 6: regB = regA >> combo(y)
            elif x == 7: regC = regA >> combo(y)
            return s if x != 0 else {'m': True, **s}
        r = reduce(kk, zip(helper_program[::2], helper_program[1::2]), {'m': False, 'output': None})

        if r['output'] == program_[-1]:
            if (ans2 := helper_fn(program_[:-1], regA)) is not None: return ans2
print(helper_fn(program, 0))