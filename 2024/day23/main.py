from functools import reduce

nodes = list(map(lambda x: x.strip().split("-"), open("input.txt")))

branches = reduce(lambda d, node: {**d,
                              node[0]: d.get(node[0], set()) | {node[1]},
                              node[1]: d.get(node[1], set()) | {node[0]}},
              nodes, {})

# part 1
networks = set()
helper_fn = lambda node, conns: (
   None if len(conns) > 3 or tuple(sorted(conns)) in networks or
   (len(conns) == 3 and not any(x.startswith('t') for x in conns))
   else (
       networks.add(tuple(sorted(conns))),
       reduce(lambda _, n: helper_fn(n, {*conns, n})
            if n not in conns and all(n in branches[_node] for _node in conns)
            else None,
            branches[node], None)
   )
)
for branch in branches: helper_fn(branch, {branch})
print(len([n for n in networks if len(n) == 3 and any(ch.startswith('t') for ch in n)]))

# part 2
networks = set()
helper_fn = lambda node, conns: (
   None if tuple(sorted(conns)) in networks
   else (
       networks.add(tuple(sorted(conns))),
       reduce(lambda _, n: helper_fn(n, {*conns, n})
            if n not in conns and all(n in branches[_node] for _node in conns)
            else None,
            branches[node], None)
   )
)
for branch in branches: helper_fn(branch, {branch})
print(",".join(sorted(max(networks, key=len))))