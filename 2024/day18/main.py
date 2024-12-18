from collections import deque
from functools import lru_cache
from bisect import bisect_left


class Pathfinder:
    def __init__(self, s, co, check = False): self.s, self.all, self.b, self.check, self.m = s, co, set(), check, [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def update_b(self, n): self.b = set(self.all[:n])

    @lru_cache(maxsize=None)
    def is_valid(self, pos): return all([0 <= pos[0] <= self.s, 0 <= pos[1] <= self.s, pos not in self.b])

    def find_path(self,):
        q = deque([(0, 0, 0)])
        seen = {(0, 0)}

        while q:
            x, y, steps = q.popleft()
            if (x, y) == (self.s, self.s): return steps if not self.check else True

            for dx, dy in self.m:
                next_pos = (x + dx, y + dy)
                if next_pos not in seen and self.is_valid(next_pos):
                    seen.add(next_pos)
                    q.append((*next_pos, steps + 1))
        return -1 if not self.check else False

    def find_blocking_coord(self):
        a, z = 0, len(self.all) - 1
        while a < z:
            m = (a + z) // 2
            self.update_b(m + 1)
            self.is_valid.cache_clear()
            a, z = (m + 1, z) if self.find_path() else (a, m)

        return self.all[a]

c = [tuple(map(int, ll.strip().split(','))) for ll in open("input.txt")]
pathfinder = Pathfinder(70, c)
# part 1:
print(pathfinder.find_path() if pathfinder.update_b(1024) is None else None)
# part 2:
pathfinder.check = True
print(*pathfinder.find_blocking_coord(), sep = ',')