from functools import lru_cache, reduce

patterns, designs = open('input.txt').read().strip().split("\n\n")
r = lru_cache(maxsize=None)(lambda design: (True, 1) if not design else reduce(
    lambda acc, p: (acc[0] or r(design[len(p):])[0], acc[1] + r(design[len(p):])[1]) if design.startswith(p) else acc,
    patterns.split(", "), (False, 0)))
# part 1
print(sum(1 for design in designs.split("\n") if r(design)[0]))
# part 2
print(sum(r(design)[1] for design in designs.split("\n")))