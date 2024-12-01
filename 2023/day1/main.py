# part 1
file = open('input.txt', 'r')
data = file.read()

helper_fn = lambda s: (next(c for c in s if c.isdigit()), next(c for c in reversed(s) if c.isdigit()))
calibration_score = sum(int(f"{nums[0]}{nums[1]}") for nums in map(helper_fn, data.strip().splitlines()))
print(calibration_score)

# part 2
number_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
second_helper_fn = lambda s: [
    number_mapping[word] if word in number_mapping else int(s[i])
    for i in range(len(s))
    for word in ([s[i]] + [w for w in number_mapping if s[i:].startswith(w)])
    if word in number_mapping or s[i].isdigit()
]
third_helper_fn = lambda s: (second_helper_fn(s)[0], second_helper_fn(s)[-1])
second_calibration_score = sum(int(f"{nums[0]}{nums[1]}") for nums in map(third_helper_fn, data.strip().splitlines()))
print(second_calibration_score)
