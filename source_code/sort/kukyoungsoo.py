"""
https://www.acmicpc.net/problem/10825
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""

N = int(input())
student = []
for num in range(N):
    temp = input().split()
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])

    student.append(temp)

for d in sorted(student, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(d[0])