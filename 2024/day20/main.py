from collections import deque
from functools import reduce
from itertools import product

def solve(file: str = "input.txt", part=1):
    m = [*map(list, open(file).read().strip().split("\n"))]
    size = (len(m), len(m[0]))
    start = next((pos for pos in product(range(size[0]), range(size[1])) if m[pos[0]][pos[1]] == 'S'))

    dist = [[*map(lambda _: -1, range(size[1]))] for _ in range(size[0])]
    dist[start[0]][start[1]] = 0

    is_valid = lambda r, c: (0 <= r < size[0] and 0 <= c < size[1] and m[r][c] != '#')

    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if not is_valid(nr, nc) or dist[nr][nc] != -1: continue
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

    if part == 1:
        special_moves = [(2, 0), (-2, 0), (-1, 1), (-1, -1),
                         (0, 2), (0, -2), (1, 1), (1, -1)]
        return sum(1
                   for r, c in product(range(size[0]), range(size[1]))
                   for dr, dc in special_moves
                   if (dist[r][c] != -1 and
                       is_valid(r + dr, c + dc) and
                       dist[r + dr][c + dc] != -1 and
                       dist[r][c] - dist[r + dr][c + dc] >= 102))

    elif part == 2:
        count = 0
        for r, c in product(range(size[0]), range(size[1])):
            if dist[r][c] == -1: continue
            for radius in range(2, 21):
                valid_points = set()
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {(r + dr, c + dc), (r + dr, c - dc),
                                   (r - dr, c + dc), (r - dr, c - dc)}:
                        if is_valid(nr, nc) and dist[nr][nc] != -1: valid_points.add((nr, nc))
                for nr, nc in valid_points:
                    if dist[r][c] - dist[nr][nc] >= 100 + radius: count += 1
        return count

print(solve(part=1))
print(solve(part=2))