def print_score():
    score = int(input("점수를 입력하세요."))

    if score > 100 or score < 0:
        print("정상적인 점수 범위가 아닙니다.")
    else:
        if score >= 80:
            print("합격입니다.")
        elif score >= 60:
            print("재시험 응시가 필요합니다.")
        else:
            print("불합격입니다.")

    while True:
        user_input = input("값을 입력하세요 : ")

        if user_input.lower() == "z":
            break

# 짝수만 출력
def print_even():
    input_number = int(input("숫자를 입력하세요."))
    index = 1
    while index <= input_number:
        if input_number % 2 == 0:
            print(index)
        index = index + 1

# 피보나치 수열 출력


def print_fibonacci_with_list():
    input_number = int(input("숫자를 입력하세요."))
    index = 1
    list = [1,1]

    while index <= input_number:
        print(list[-1])
        list.append(list[-1] + list[-2])


def print_fibonacci_with_variables():
    input_number = int(input("숫자를 입력하세요."))
    a = 1
    b = 1
    c = 1

    while c <= input_number:
        c = a + b
        print(c)
        a = b
        b = c

def repeat_function():
    i = 1

    while i <=5:
        print_score()
        i = i + 1

# 함수 호출 방법
# repeat_function()
#
# arr = ['AA', 'BB', 'CC', 'DD']
#
# for i in arr:
#     print(i)

test = [
    {
        'name': 'aaa',
        'number': 10101,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'bbb',
        'number': 10102,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ccc',
        'number': 10103,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
  {
        'name': 'ddd',
        'number': 10104,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'eee',
        'number': 10105,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    }
]

correct_answer = {
    'math':[1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'korean':[1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'english':[1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'science':[1, 3, 2, 4, 5, 3, 1, 2, 3, 4]
}


# 학생의 점수 구하기
def get_score(student_answer, correct_answer):
    score = 0
    for (student, correct) in zip(student_answer, correct_answer):
        #print(student, '/', correct)
        if student == correct:
            score = score + 10
    #print(score)
    return score

for student in test:
    if student['name'] == 'ccc': # 배열 반복에서 스킵하는 방법
        continue

    print("학생", student['name'], "==================")
    math_score = get_score(student['math'], correct_answer['math'])
    korean_score = get_score(student['korean'], correct_answer['korean'])
    english_score = get_score(student['english'], correct_answer['english'])
    science_score = get_score(student['science'], correct_answer['science'])

    print("수학점수:", math_score)
    print("국어점수:", korean_score)
    print("영어점수:", english_score)
    print("과학점수:", science_score)