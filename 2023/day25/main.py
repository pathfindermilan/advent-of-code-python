import random
from collections import defaultdict

data = open('input.txt').read().strip()
l = data.split("\n")
random.seed(42)

g = defaultdict(list)
_ = list(
    map(
        lambda ll: [
            g[ll.split(": ")[0]]
                .extend(ll.split(": ")[1]
                .split()) or
            [g[c].append(ll.split(": ")[0])

            for c in ll.split(": ")[1].split()]
        ],
    l))

def min_cut(gr):
    mrg = {n: {n} for n in gr}

    while len(gr) > 2:
        k = random.choice(list(gr.keys()))
        v = random.choice(gr[k])
        mrg[k].update(mrg[v])

        gr[k].extend(gr[v])
        for n in gr[v]: gr[n] = [k if x == v else x for x in gr[n]]
        gr[k] = [x for x in gr[k] if x != k]
        del gr[v]
        del mrg[v]
    return len(list(gr.values())[0]), [len(ver) for ver in mrg.values()]

def monte_carlo(gr, itr=30):
    m_cut = float('inf')
    two_parts = None

    for _ in range(itr):
        gg = {k: v[:] for k, v in gr.items()}
        cut, parts = min_cut(gg)
        if cut < m_cut: m_cut, two_parts = cut, parts
    return m_cut, two_parts

m_cut, components = monte_carlo(g, itr=2)
if m_cut == 3: print(components[0] * components[1])
else: print("min cut is not 3!")