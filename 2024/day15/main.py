import re
from typing import List, Tuple
from collections import OrderedDict

helper_mapa, moves = open('input.txt').read().strip().split('\n\n')
p = r"@"

moves = "".join(moves.splitlines())
move_dir = lambda m: {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}.get(m, (0, 0))

# part 1
process_mapa = lambda: next(
    ((list(map(list, helper_mapa.split("\n"))), index, match.start())
     for index, row in enumerate(helper_mapa.split("\n"))
     for match in re.finditer(p, row)),
    (list(map(list, helper_mapa.split("\n"))), None, None)
)
mapa1, start_row, start_col = process_mapa()
ROW, COL = len(mapa1), len(mapa1[0])

for move in moves:
    dr, dc = move_dir(move)
    t = []
    helper_row, helper_col = start_row, start_col
    while (char := mapa1[helper_row := helper_row + dr][helper_col := helper_col + dc]) != '#':
        if char == 'O': t.append((helper_row, helper_col))
        if char == '.': break
    else: continue
    mapa1[start_row][start_col], mapa1[start_row + dr][start_col + dc] = '.', '@'
    for box_row, box_col in t: mapa1[box_row + dr][box_col + dc] = 'O'
    start_row, start_col = start_row + dr, start_col + dc

print(sum(100 * r + c for r in range(ROW) for c in range(COL) if mapa1[r][c] == 'O'))


# part 2
rules = {"#": "##", "O": "[]", ".": "..", "@": "@."}
def process_mapa(helper_mapa: str, expand_char: dict) -> Tuple[List[List[str]], int | None, int | None]:
    expanded_map = [list("".join(expand_char[ch] for ch in line)) for line in helper_mapa.splitlines()]
    for row_idx, row in enumerate(expanded_map):
        for col_idx, char in enumerate(row):
            if char == "@": return expanded_map, row_idx, col_idx

mapa2, start_row, start_col = process_mapa(helper_mapa, rules)
ROW, COL = len(mapa2), len(mapa2[0])

for move in moves:
    dr, dc = move_dir(move)
    t = [(start_row, start_col)]
    t_dict = OrderedDict()
    helper_row, helper_col = start_row, start_col
    while (char := mapa2[helper_row := t[0][0] + dr][helper_col := t[0][1] + dc]) != '#':
        if (helper_row, helper_col) not in t_dict:
            if char == "[":
                t.extend([(helper_row, helper_col), (helper_row, helper_col + 1)])
                t_dict[(helper_row, helper_col)] = char
                t_dict[(helper_row, helper_col + 1)] = mapa2[helper_row][helper_col + 1]
            elif char == "]":
                t.extend([(helper_row, helper_col), (helper_row, helper_col - 1)])
                t_dict[(helper_row, helper_col)] = char
                t_dict[(helper_row, helper_col - 1)] = mapa2[helper_row][helper_col - 1]
        if mapa2[t[0][0]][t[0][1]] in ["[", "]", "@"]: t = t[1:]
        if len(t) == 0: break
    else: continue

    for tr, tc in list(t_dict.keys())[::-1]:
        if 0 <= tr + dr < ROW and 0 <= tc + dc < COL: mapa2[tr + dr][tc + dc] = t_dict[(tr, tc)]
        mapa2[tr][tc] = "."
    mapa2[start_row][start_col], mapa2[start_row + dr][start_col + dc] = '.', '@'
    start_row, start_col = start_row + dr, start_col + dc

print(sum(100 * r + c for r in range(ROW) for c in range(COL) if mapa2[r][c] == "["))