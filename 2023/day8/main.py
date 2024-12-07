import re

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

    side = 0 if ch == "L" else 1
    helper = dict_routes[helper][side]
    ans += 1
print(ans)

# part 2

