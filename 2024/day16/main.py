from collections import deque
import heapq

mapa = [list(ll) for ll in open('input.txt').read().strip().split("\n")]
start_position = next((index_r, index_c) for index_r in range(len(mapa)) for index_c in range(len(mapa[0])) if mapa[index_r][index_c] == 'S')
end_position = next((index_r, index_c) for index_r in range(len(mapa)) for index_c in range(len(mapa[0])) if mapa[index_r][index_c] == 'E')

generate_moves = lambda path_cost, r, c, dr, dc: [
    (path_cost + 1, r + dr, c + dc, dr, dc),
    (path_cost + 1000, r, c, dc, -dr),
    (path_cost + 1000, r, c, -dc, dr)
]

# part 1
m_distance = lambda r, c: abs(r - end_position[0]) + abs(c - end_position[1])
start_state = (*start_position, 0, 1)
hq = [(m_distance(*start_position), 0, *start_state)]
min_costs = {start_state: 0}
final_states = set()

while hq:
    total_cost, path_cost, r, c, dr, dc = heapq.heappop(hq)
    current_state = (r, c, dr, dc)

    if path_cost > min_costs.get(current_state, float("inf")): continue
    if (r, c) == end_position:
        final_states.add(current_state)
        break

    for new_path_cost, nr, nc, ndr, ndc in generate_moves(path_cost, r, c, dr, dc):
        next_state = (nr, nc, ndr, ndc)
        if mapa[nr][nc] == "#": continue
        if new_path_cost >= min_costs.get(next_state, float("inf")): continue

        min_costs[next_state] = new_path_cost
        new_total_cost = new_path_cost + m_distance(nr, nc)
        heapq.heappush(hq, (new_total_cost, new_path_cost, *next_state))

print(path_cost)

# part 2
m_distance = lambda r, c: abs(r - end_position[0]) + abs(c - end_position[1])
start_state = (*start_position, 0, 1)

hq = [(m_distance(*start_position), 0, *start_state)]
min_costs, pr, final_states = {start_state: 0}, dict(), set()
min_cost = float("inf")

while hq:
    total_cost, path_cost, r, c, dr, dc = heapq.heappop(hq)
    current_state = (r, c, dr, dc)

    if path_cost > min_costs.get(current_state, float("inf")): continue
    if (r, c) == end_position:
        if path_cost > min_cost: break
        min_cost = path_cost
        final_states.add(current_state)

    for new_path_cost, nr, nc, ndr, ndc in generate_moves(path_cost, r, c, dr, dc):
        next_state = (nr, nc, ndr, ndc)
        if mapa[nr][nc] == "#": continue
        min_cost = min_costs.get(next_state, float("inf"))
        if new_path_cost > min_cost: continue

        if new_path_cost < min_cost:
            pr[next_state] = set()
            min_costs[next_state] = new_path_cost

        pr[next_state].add(current_state)
        new_total_cost = new_path_cost + m_distance(nr, nc)
        heapq.heappush(hq, (new_total_cost, new_path_cost, *next_state))

path_queue, visited = deque(final_states), set(final_states)
while path_queue:
    current = path_queue.popleft()
    for prev in pr.get(current, set()):
        if prev in visited: continue
        visited.add(prev)
        path_queue.append(prev)

print(len({(r, c) for r, c, _, _ in visited}))