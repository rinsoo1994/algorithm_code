int_list = [int(data) for data in input()]


def make_max_num(x, y):
    if x <= 1 or y <= 1:
        return x + y
    else:
        return x * y


result = 0
for data in int_list:
    result = make_max_num(result, data)


print(result)
