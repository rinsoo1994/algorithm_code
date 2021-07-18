"""
5 3
1
2
8
4
9
"""

"""
공유기 설치 길이를 움직여(이분탐색하여) 적절한 집에 설치 가능한지 살펴보는 문제다.

1) 거리가 주어지면, 해당 라우터를 몇 개 설치할 수 있는지 산출하는 router_counter 함수를 정의한다.
2) 첫 집을 start로, 첫 집과 끝집의 차이를 end로 둔다.
3-1) 해당 거리로 충분한 설치 장소를 찾지 못했다면 거리를 줄여주고
3-2) 설치된 집이 더 많다면 거리를 늘려준다.

"""


N, C = map(int, input().split())
house = []
for num in range(N):
    house.append(int(input()))


# 해당 거리를 유지하며 공유기가 몇 개 가능한지?
def router_counter(distance):
    count = 1
    cur_house = house[0]  # 시작점
    for i in range(1, N):  # 집 모두를 돈다
        if cur_house + distance <= house[i]:  # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_house = house[i]  # 공유기 설치된 집 갱신
    return count


house = sorted(house)  # 이분탐색을 위한 정렬
start, end = 1, house[-1] - house[0]  # 1, 첫집과 끝집

while start <= end:  # 이분탐색 알고리즘
    mid = (start + end) // 2
    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
        print("start", start)

    else:
        end = mid - 1
        print("end", end)

print(answer)
