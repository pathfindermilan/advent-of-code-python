# part 1
file = open('input.txt', 'r')
data = file.read()

helper_fn = lambda line: (
    int(line.split(':')[0].split()[1]),
    tuple(
        (color, set.strip().split()[0]) for data_to_count in line.split(':')[1].split(';')
            for set in data_to_count.strip().split(',')
            for color in ['red', 'green', 'blue']
                if color in set.strip().split()[1]
    )
)

second_helper_fn = lambda t: (
    helper_fn(t)[0],
    all((c == "red" and int(count) <= 12) or
        (c == "green" and int(count) <= 13) or
        (c == "blue" and int(count) <= 14)
        for c, count in helper_fn(t)[1])
)

sum_of_the_IDs = sum(nums[0] for nums in map(second_helper_fn, data.strip().splitlines()) if nums[1])
print(sum_of_the_IDs)

# part 2
third_helper_fn = lambda t: (
    helper_fn(t)[0],
    *{color: max(int(count) for c, count in helper_fn(t)[1] if c == color) for color in ['red', 'green', 'blue']}.values()
)

second_sum_of_the_IDs = sum(nums[1] * nums[2] * nums[3] for nums in map(third_helper_fn, data.strip().splitlines()))
print(second_sum_of_the_IDs)