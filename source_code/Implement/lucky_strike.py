data = input()

length = len(data)

first_sum = 0
second_sum = 0
for idx in range(int(length/2)):
    first_sum += int(data[idx])

for idx in range(int(length/2), length):
    second_sum += int(data[idx])

print(first_sum, second_sum)
if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")