from collections import deque, defaultdict
from functools import reduce, lru_cache

calc = lru_cache(maxsize=None)(lambda n: reduce(lambda x, f: f(x), [
    lambda n: (n ^ (n * 64)) % 16777216,
    lambda n: (n ^ (n // 32)) % 16777216,
    lambda n: (n ^ (n * 2048)) % 16777216
], n))

i = lambda n, times: reduce(lambda x, _: calc(x), range(times), n)

ans1 = sum(i(int(ll.strip()), 2000) for ll in open("input.txt"))
print(ans1)

# part 2

max_bananas = defaultdict(int)

for ll in open("input.txt"):
    n = int(ll)
    last_digits = [n % 10]
    for _ in range(2000):
        n = calc(n)
        last_digits.append(n % 10)
    visited = set()
    for i in range(len(last_digits) - 4):
        pattern = tuple(last_digits[j + 1] - last_digits[j] for j in range(i, i + 4))
        if pattern not in visited:
            visited.add(pattern)
            max_bananas[pattern] += last_digits[i + 4]
print(max(max_bananas.values()))


