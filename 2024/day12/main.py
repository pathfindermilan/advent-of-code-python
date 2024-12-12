data = open('input.txt').read().strip()
l = data.split('\n')
mapa = [list(ll.strip()) for ll in l]

def solve(gr):
    row, col = len(gr), len(gr[0])
    visited = [[False] * col for _ in range(row)]
    regions = []

    def find_region(r, c):
        stack, region = [(r, c)], set()
        x = lambda rr, cc: [(rr - 1, cc), (rr + 1, cc), (rr, cc - 1), (rr, cc + 1)]

        while stack:
            curr_r, curr_c = stack.pop()
            if (curr_r, curr_c) not in region:
                region.add((curr_r, curr_c))
                stack.extend((rrr, ccc) for rrr, ccc in x(curr_r, curr_c)
                             if 0 <= rrr < row and 0 <= ccc < col
                             and gr[rrr][ccc] == gr[r][c] and (rrr, ccc) not in region)
        return region

    def perimeter(region):
        return sum(4 - sum((x+xx, y+yy) in region for xx, yy in [(-1,0), (1,0), (0,-1), (0,1)]) for x, y in region)

    def sides(region):
        region = set(region)
        count = 0
        c = set()
        for x, y in region: c.update([(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)])

        for x, y in c:
            dir = [(x - 1, y - 1), (x - 1, y), (x, y), (x, y - 1)]
            helper = sum(1 for d in dir if d in region)
            if helper == 1: count += 1
            elif helper == 2:
                dig = (dir[0] in region and dir[2] in region) or (dir[1] in region and dir[3] in region)
                if dig: count += 2
            elif helper == 3: count += 1
        return count

    for r in range(row):
        for c in range(col):
            if not visited[r][c]:
                region = find_region(r, c)
                regions.append(region)
                _ = [visited[rr].__setitem__(cc, True) for rr, cc in region]

    part1 = sum(len(region) * perimeter(region) for region in regions)
    part2 = sum(len(region) * sides(region) for region in regions)
    return part1, part2

ans1, ans2 = solve(mapa)
print(ans1, ans2)