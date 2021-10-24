"""
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

iter_num = int(input())

student_list = []
for i in range(iter_num):
    student_score = input().split(" ")
    student_list.append([student_score[0], int(student_score[1]), int(student_score[2]), int(student_score[3])])

result = sorted(student_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for res in result:
    print(res[0])