data_list = list(map(int, input()))

zero_group = 0
group_count = {0: 0, 1: 0}
temp_group = -1

for data in data_list:
    if temp_group == data:
        continue
    temp_group = data
    group_count[temp_group] += 1

print(min(list(group_count.values())))
