import re
from collections import defaultdict, Counter
from functools import cmp_to_key

p = r"\d+"
l = open('input.txt').read().strip().split("\n")

def compare_hands(a, b):
    for i in range(len(a[0])):
        if dict_strength[a[0][i]] != dict_strength[b[0][i]]:
            return dict_strength[b[0][i]] - dict_strength[a[0][i]]
    return 0

# part 1
five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
dict_strength = {
    "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13,
}

for ll in l:
    house, bid = ll.split(" ")
    bid = int(bid)

    char_counts = Counter(house)

    if 5 in char_counts.values(): five_of_kind.append((house, bid))
    elif 4 in char_counts.values(): four_of_kind.append((house, bid))
    elif 3 in char_counts.values() and len(char_counts) == 2: full_house.append((house, bid))
    elif 3 in char_counts.values() and len(char_counts) == 3: three_of_kind.append((house, bid))
    elif 2 in char_counts.values() and len(char_counts) == 3: two_pair.append((house, bid))
    elif 2 in char_counts.values() and len(char_counts) == 4: one_pair.append((house, bid))
    elif 1 in char_counts.values(): high_card.append((house, bid))

five_of_kind.sort(key=lambda x: dict_strength[x[0][0]])
four_of_kind.sort(key=cmp_to_key(compare_hands), reverse=True)
full_house.sort(key=cmp_to_key(compare_hands), reverse=True)
three_of_kind.sort(key=cmp_to_key(compare_hands), reverse=True)
two_pair.sort(key=cmp_to_key(compare_hands), reverse=True)
one_pair.sort(key=cmp_to_key(compare_hands), reverse=True)
high_card.sort(key=cmp_to_key(compare_hands), reverse=True)

all_sorted = high_card + one_pair + two_pair + three_of_kind + full_house + four_of_kind + five_of_kind

ans = 0
for index, hand in enumerate(all_sorted):
    ans += (index + 1) * hand[1]
print(ans)


# part 2
five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
dict_strength = {
    "J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13,
}

for ll in l:
    house, bid = ll.split(" ")
    bid = int(bid)

    char_counts = Counter(house)
    copy_char_counts = char_counts.copy()
    J_count = copy_char_counts.pop("J", 0)
    helper = max(copy_char_counts.values()) if copy_char_counts else 0

    if 5 == (helper + J_count): five_of_kind.append((house, bid))
    elif 4 == (helper + J_count): four_of_kind.append((house, bid))
    elif 3 == (helper + J_count) and (len(char_counts) == 3 if J_count >= 1 else len(char_counts) == 2): full_house.append((house, bid))
    elif 3 == (helper + J_count) and (len(char_counts) == 4 if J_count >= 1 else len(char_counts) == 3): three_of_kind.append((house, bid))
    elif 2 in char_counts.values() and len(char_counts) == 3: two_pair.append((house, bid))
    elif 2 == (helper + J_count) and (len(char_counts) == 5 if J_count == 1 else len(char_counts) == 4): one_pair.append((house, bid))
    elif 1 in char_counts.values() and J_count == 0: high_card.append((house, bid))

five_of_kind.sort(key=cmp_to_key(compare_hands), reverse=True)
four_of_kind.sort(key=cmp_to_key(compare_hands), reverse=True)
full_house.sort(key=cmp_to_key(compare_hands), reverse=True)
three_of_kind.sort(key=cmp_to_key(compare_hands), reverse=True)
two_pair.sort(key=cmp_to_key(compare_hands), reverse=True)
one_pair.sort(key=cmp_to_key(compare_hands), reverse=True)
high_card.sort(key=cmp_to_key(compare_hands), reverse=True)

all_sorted = high_card + one_pair + two_pair + three_of_kind + full_house + four_of_kind + five_of_kind

ans = 0
for index, hand in enumerate(all_sorted):
    ans += (index + 1) * hand[1]
print(ans)