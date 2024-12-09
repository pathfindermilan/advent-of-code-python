data = open('input.txt').read().strip()
data_list_ = []
all_dots = dict()
all_numbers = dict()
counter = 0
helper = 0
for i, char in enumerate(data):
    x = int(char)
    if i % 2 == 0:
        if x != 0:
            data_list_.extend([counter] * x)
            all_numbers[counter] = (helper, x)
            helper += x
        counter += 1
    else:
        data_list_.extend([-1] * x)
        if x != 0:
            all_dots[helper] = x
            helper += x
# part 1
data_list = data_list_.copy()
counter = 0
numbers = [(index, i) for index, i in enumerate(data_list) if i >-1]
for key_dot, value_dot in all_dots.items():
    for index, i in enumerate(range(value_dot)):
        try:
            index_x, x = numbers.pop()
            counter += 1
            data_list[key_dot + index] = x
        except IndexError:
            break
    else: continue
    break
print(sum(i * x for i, x in enumerate(data_list[:len(data_list)-counter]) if i > -1))

# part 2
all_dots_list = list(all_dots.items())
for number in range(len(all_numbers) - 1, -1, -1):
    index_x, x = all_numbers[number]
    for i, (key_dot, value_dot) in enumerate(all_dots_list):
        if key_dot >= index_x:
            all_dots_list = all_dots_list[:i]
            break
        if x <= value_dot:
            all_numbers[number] = (key_dot, x)
            if x == value_dot: all_dots_list.pop(i)
            else: all_dots_list[i] = (key_dot + x, value_dot - x)
            break
print(sum(i * number for i, (index_x, x) in all_numbers.items() for number in range(index_x, index_x + x)))

