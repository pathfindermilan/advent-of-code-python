import re
import time
from collections import Counter

data = open('input.txt').read().strip()
l = data.split("\n\n")

p = r"\d+"
s2s_array = []
s2f_array = []
f2w_array = []
w2l_array = []
l2t_array = []
t2h_array = []
h2l_array = []

seeds = [seed for seed in map(int, re.findall(p, l[0].split(":")[1]))]

s2s_string = l[1].split(":")[1].split("\n")[1:]
for s2s in s2s_string:
    s2s_array.append([s2s_ for s2s_ in map(int, re.findall(p, s2s))])

s2f_string = l[2].split(":")[1].split("\n")[1:]
for s2f in s2f_string:
    s2f_array.append([s2f_ for s2f_ in map(int, re.findall(p, s2f))])

f2w_string = l[3].split(":")[1].split("\n")[1:]
for f2w in f2w_string:
    f2w_array.append([f2w_ for f2w_ in map(int, re.findall(p, f2w))])

w2l_string = l[4].split(":")[1].split("\n")[1:]
for w2l in w2l_string:
    w2l_array.append([w2l_ for w2l_ in map(int, re.findall(p, w2l))])

l2t_string = l[5].split(":")[1].split("\n")[1:]
for l2t in l2t_string:
    l2t_array.append([l2t_ for l2t_ in map(int, re.findall(p, l2t))])

t2h_string = l[6].split(":")[1].split("\n")[1:]
for t2h in t2h_string:
    t2h_array.append([t2h_ for t2h_ in map(int, re.findall(p, t2h))])

h2l_string = l[7].split(":")[1].split("\n")[1:]
for h2l in h2l_string:
    h2l_array.append([h2l_ for h2l_ in map(int, re.findall(p, h2l))])

def get_location(seed):
    s2s_helper = seed
    for d_s2s, s_s2s, r_s2s in s2s_array:
        if seed in range(s_s2s, s_s2s + r_s2s):
            s2s_helper = seed - s_s2s + d_s2s
            break
    s2f_helper = s2s_helper
    for d_s2f, s_s2f, r_s2f in s2f_array:
        if s2s_helper in range(s_s2f, s_s2f + r_s2f):
            s2f_helper = s2s_helper - s_s2f + d_s2f
            break
    f2w_helper = s2f_helper
    for d_f2w, s_f2w, r_f2w in f2w_array:
        if s2f_helper in range(s_f2w, s_f2w + r_f2w):
            f2w_helper = s2f_helper - s_f2w + d_f2w
            break
    w2l_helper = f2w_helper
    for d_w2l, s_w2l, r_w2l in w2l_array:
        if f2w_helper in range(s_w2l, s_w2l + r_w2l):
            w2l_helper = f2w_helper - s_w2l + d_w2l
            break
    l2t_helper = w2l_helper
    for d_l2t, s_l2t, r_l2t in l2t_array:
        if w2l_helper in range(s_l2t, s_l2t + r_l2t):
            l2t_helper = w2l_helper - s_l2t + d_l2t
            break
    t2h_helper = l2t_helper
    for d_t2h, s_t2h, r_t2h in t2h_array:
        if l2t_helper in range(s_t2h, s_t2h + r_t2h):
            t2h_helper = l2t_helper - s_t2h + d_t2h
            break
    h2l_helper = t2h_helper
    for d_h2l, s_h2l, r_h2l in h2l_array:
        if t2h_helper in range(s_h2l, s_h2l + r_h2l):
            h2l_helper = t2h_helper - s_h2l + d_h2l
            break
    return h2l_helper

def get_location_for_range(range_start, range_end):
    return 0

# part 1
locations = []
for seed in seeds:
    start_time = time.time()
    h2l_helper = get_location(seed)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    locations.append(h2l_helper)
print(min(locations))

# part 2

# locations = []
# for i in range(0, len(seeds) - 1, 2):
#     start, length = seeds[i], seeds[i + 1]
#     loc = get_location_for_range(start, start+length)
#     locations.append(loc)
# print(min(locations))

