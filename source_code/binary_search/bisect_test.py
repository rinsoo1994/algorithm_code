from bisect import bisect_left, bisect_right

this_list = ["aab", "aac"]
result = bisect_left(this_list, "aaa")
print(result)
result = bisect_right(this_list, "aaz")
print(result)