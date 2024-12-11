import numpy as np
import sympy as sp
import re

p = r'-?\d+'
data = open('input.txt').read().strip()
l = data.split('\n')
h = [tuple(map(int, re.findall(p, ll))) for ll in l]
MIN_COORD = 200000000000000
MAX_COORD = 400000000000000

def solve_system(h):
    x, y, z, vx, vy, vz = sp.symbols("x y z vx vy vz")
    t = sp.symbols("t:3")
    eq = []

    for i, (x0, y0, z0, vx0, vy0, vz0) in enumerate(h[:3]):
        eq.extend([
            sp.Eq(x + vx * t[i] - x0 - vx0 * t[i], 0),
            sp.Eq(y + vy * t[i] - y0 - vy0 * t[i], 0),
            sp.Eq(z + vz * t[i] - z0 - vz0 * t[i], 0)
        ])

    s = sp.solve(eq, (x, y, z, vx, vy, vz, t[0], t[1], t[2]), dict=True)
    if s: return s[0][x], s[0][y], s[0][z]
    return None

def intersect(h1, h2):
    x1, y1, _, vx1, vy1, _ = h1
    x2, y2, _, vx2, vy2, _ = h2
    a = np.array([[vx1, -vx2], [vy1, -vy2]])
    b = np.array([x2 - x1, y2 - y1])

    if np.linalg.det(a) == 0: return None

    try: t1, t2 = np.linalg.solve(a, b)
    except np.linalg.LinAlgError: return None

    if t1 < 0 or t2 < 0: return None
    x = x1 + vx1 * t1
    y = y1 + vy1 * t1
    return x, y

# part 1
ans = sum(1 for i, hs1 in enumerate(h)
          for hs2 in h[:i]
          if (intersection := intersect(hs1, hs2))
          and MIN_COORD <= intersection[0] <= MAX_COORD
          and MIN_COORD <= intersection[1] <= MAX_COORD)
print(ans)


# Part 2
solution = solve_system(h)
x, y, z = solution
print(int(x + y + z))
