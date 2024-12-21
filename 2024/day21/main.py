from collections import deque
from functools import lru_cache
from itertools import product

class Solver:
    def __init__(self, num):
        self.num = num
        self.num_keypad = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"]
        ]
        self.dir_keypad = [
            [None, "^", "A"],
            ["<", "v", ">"]
        ]
        self.__num_seqs = self.__compute_seqs(self.num_keypad)
        self.__dir_seqs = self.__compute_seqs(self.dir_keypad)
        self.__dir_lengths = {key: len(value[0]) for key, value in self.__dir_seqs.items()}

    def __compute_seqs(self, keypad):
        pos = { keypad[r][c]: (r, c) for r in range(len(keypad)) for c in range(len(keypad[r])) if keypad[r][c] is not None }

        s = {}
        for x in pos:
            for y in pos:
                if x == y:
                    s[(x, y)] = ["A"]
                    continue

                p = list()
                q = deque([(pos[x], "")])
                m = float("inf")

                while q:
                    (r, c), moves = q.popleft()
                    for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                        if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                        if keypad[nr][nc] is None: continue

                        if keypad[nr][nc] == y:
                            if m < len(moves) + 1: break
                            m = len(moves) + 1
                            p.append(moves + nm + "A")
                        else: q.append(((nr, nc), moves + nm))
                    else: continue
                    break
                s[(x, y)] = p
        return s

    @lru_cache
    def __compute_length(self, seq, d: int = None):
        d = d or self.num
        return (
            sum(self.__dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
            if d == 1
            else sum(
                min(self.__compute_length(subseq, d - 1) for subseq in self.__dir_seqs[(x, y)])
                for x, y in zip("A" + seq, seq)
            )
        )

    def __compute(self, string):
        return list(
            map(lambda x: "".join(x), product(*[self.__num_seqs[(x, y)] for x, y in zip("A" + string, string)])))

    def process(self, d):
        return sum(
            min(map(self.__compute_length, self.__compute(ll))) * int(ll[:-1]) for ll in d
        )

data = open("input.txt").read().strip().splitlines()
# part 1
solver = Solver(num=2)
ans1 = solver.process(data)
print(ans1)

# part 2
solver = Solver(num=25)
ans2 = solver.process(data)
print(ans2)