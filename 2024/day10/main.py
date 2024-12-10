from collections import deque
import re

data = open('input.txt').read()

def a_star(input_data):
    l = input_data.strip().split("\n")
    mapa = []
    [mapa.append(list(map(int, re.findall("\d", ll)))) for ll in l]
    row, col = len(mapa), len(mapa[0])
    zeros = [(r, c) for r in range(row) for c in range(col)
                    if mapa[r][c] == 0]

    def count(r, c):
        q = deque([(r, c)])
        visited = {(r, c)}
        trailheads = set()

        while q:
            curr_row, curr_col = q.popleft()

            if mapa[curr_row][curr_col] == 9:
                trailheads.add((curr_row, curr_col))
                continue

            for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col),
                                     (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
                if not (0 <= next_row < row and 0 <= next_col < col): continue
                if mapa[next_row][next_col] != mapa[curr_row][curr_col] + 1: continue
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    q.append((next_row, next_col))

        return len(trailheads)

    unique_paths = sum(count(row, col) for row, col in zeros)
    return unique_paths

ans1 = a_star(data)
print(ans1)