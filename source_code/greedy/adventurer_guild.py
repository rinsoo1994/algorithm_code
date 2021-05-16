N = int(input())
member_list = list(map(int, input().split()))

member_list.sort()
result = 0
count = 0
for member in member_list:
    count += 1
    if count >= member:
        result += 1
        count = 0

print(result)