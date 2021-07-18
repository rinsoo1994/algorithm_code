def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x, reverse=True)
    print(numbers)
    # for number in numbers:
        # print(number*5)
    return str(int(''.join(numbers)))


result = solution([6, 10, 2])
print(result)

