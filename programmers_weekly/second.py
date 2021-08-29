
def check_grade(average):
    if average >= 90:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 70 <= average < 80:
        grade = "C"
    elif 50 <= average < 70:
        grade = "D"
    else:
        grade = "F"

    return grade


def solution(scores):
    answer = ''
    for i, score in enumerate(zip(*scores)):

        if (min(score) == score[i] or max(score) == score[i]) and score.count(score[i]) == 1:
            average = (sum(score) - score[i]) / (len(scores) - 1)
        else:
            average = sum(score) / len(scores)

        grade = check_grade(average)
        answer += grade

    return answer


result = solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	)
print(result)