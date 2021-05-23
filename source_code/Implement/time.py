N = int(input())

count = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            now = f"{h} {m} {s}"
            if "3" in now:
                count += 1

print(count)