import time

data = open('input.txt').read().strip()
M = [list(row) for row in data.split('\n')]
h, w = len(M), len(M[0])
row, col = next((i, j) for i, row in enumerate(M) for j, c in enumerate(row) if c == '^')

# part 1

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
where = 0
visited = set()
current_start, current_end = row, col

while True:
    visited.add((current_start, current_end))
    rr, cc = dir[where]
    r, c = current_start + rr, current_end + cc

    if not (0 <= r < h and 0 <= c < w):
        break

    if M[r][c] == '#':
        where = (where + 1) % 4
    else:
        current_start, current_end = r, c
print(len(visited))

# part 2
start_time = time.time()

ans = 0
for i, j in visited:
    M[i][j] = "#"
    current_r, current_c = row, col
    where = 0
    new_visited = set()

    while True:
        rr, cc = dir[where]
        # new_visited.add((current_r, current_c))
        new_visited.add((current_r, current_c, rr, cc))
        r, c = current_r + rr, current_c + cc

        if not (0 <= r < h and 0 <= c < w):
            break

        if M[r][c] == '#':
            where = (where + 1) % 4
        else:
            current_r, current_c = r, c

        if (r, c, rr, cc) in new_visited:
            ans += 1
            break
    M[i][j] = "."
print(ans)

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)