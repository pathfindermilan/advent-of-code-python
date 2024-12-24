values, relations = open("input.txt").read().split("\n\n")
calc = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}

# part 1
def score(output):
    if output not in true_values:
        input1, operation, input2 = true_relations[output]
        if operation not in calc:
            raise ValueError(f"Invalid operation: {operation} for {output}")
        true_values[output] = calc[operation](score(input1), score(input2))
    return true_values[output]

true_values = dict(map(lambda x: (x.split(": ")[0], int(x.split(": ")[1])), values.split("\n")))
true_relations = dict(map(lambda x: (x.split()[4], tuple(x.split()[:3])), relations.split("\n")))

for key in true_relations.keys(): _ = score(key)
string_number = "".join(str(v) for k, v in sorted(
    filter(lambda x: x[0].startswith("z"), true_values.items()),
    key=lambda x: int(x[0][1:])
))
print(int(string_number[::-1], 2))

# part 2
# ...