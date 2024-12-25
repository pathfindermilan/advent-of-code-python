# part 1

locks, keys = [], []
for d in open("input.txt").read().strip().split("\n\n"):
    holder = [sum(1 for r in d.split("\n") for c,v in enumerate(r) if v=="#" and c==i) for i in range(5)]
    (locks if "#" in d.split("\n")[0] else keys).append(holder)

generate_combinations = lambda locks, keys: [[l + k for l, k in zip(lock, key)] for lock in locks for key in keys]
all_combinations = generate_combinations(locks, keys)
print(f"Solution for Part 1: {sum(all(num <= 7 for num in combination) for combination in all_combinations)}")

# part 2
def print_colorful_tree(height=5):
    GREEN = '\033[32m'
    RED = '\033[31m'
    BROWN = '\033[33m'
    RESET = '\033[0m'

    for i in range(height):
        print(' ' * (height - i - 1), end='')
        for j in range(2 * i + 1):
            if j % 2 == 0: print(f"{GREEN}*{RESET}", end='')
            else: print(f"{RED}o{RESET}", end='')
        print()
    for i in range(2): print(' ' * (height - 2) + f"{BROWN}|||{RESET}")

print("For Part 2: Hmmmmm..... \n\nMerry Christmas\n")
print_colorful_tree(5)