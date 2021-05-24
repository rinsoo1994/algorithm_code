"""
K1KA5CB7
AJKDLSI412K4JSJ9D
"""
string = input()
sorted_string = sorted(string)

sum_total = 0
result = ""
for d in sorted_string:
    if d.isdigit():
        sum_total += int(d)
    else:
        result += d

if sum_total:
    result += str(sum_total)

print(result)
