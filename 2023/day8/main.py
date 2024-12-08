import re
from math import gcd
from functools import reduce
from math import lcm

data = open('input.txt').read().strip()
pathway, routes = data.split("\n\n")

dict_routes = dict()
for route in routes.split("\n"):
    k, vals = route.split(" = ")

    val1, val2 = vals.strip().split(", ")
    val1, val2 = val1[1:], val2[:-1]
    dict_routes[k] = (val1, val2)

# part 1
helper = "AAA"
ans = 0
pathway_iter = iter(pathway)

while helper != "ZZZ":
    try:
        ch = next(pathway_iter)
    except StopIteration:
        pathway_iter = iter(pathway)
        ch = next(pathway_iter)

    helper = dict_routes[helper][0 if ch == "L" else 1]
    ans += 1
print(ans)

# part 2
all_arrays_with_counts = []
all_A = [k for k in dict_routes.keys() if k.endswith("A")]

for one_A in all_A:
    pathway_iter = iter(pathway)
    one_array_with_counts = []
    helper = one_A
    count = 0
    keep_all_z_positions = []
    while True:
        while count == 0 or not helper.endswith("Z"):
            try:
                ch = next(pathway_iter)
            except StopIteration:
                pathway_iter = iter(pathway)
                ch = next(pathway_iter)

            helper = dict_routes[helper][0 if ch == "L" else 1]
            count += 1
        one_array_with_counts.append(count)
        if helper not in keep_all_z_positions:
            keep_all_z_positions.append(helper)
            count = 0
        elif helper in keep_all_z_positions:
            break
    all_arrays_with_counts.append(one_array_with_counts)

periods = [i[0] for i in all_arrays_with_counts]
print(reduce(lcm, periods))