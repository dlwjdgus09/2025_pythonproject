# def print_times_table(number):
#     print(number, "*", 1, "=", number*1)
#     print(number, "*", 2, "=", number*2)
#     print(number, "*", 3, "=", number*3)
#     print(number, "*", 4, "=", number*4)
#     print(number, "*", 5, "=", number*5)
#     print(number, "*", 6, "=", number*6)
#     print(number, "*", 7, "=", number*7)
#     print(number, "*", 8, "=", number*8)
#     print(number, "*", 9, "=", number*9)
#
#
# while True:
#     user_input = input("값을 입력하세요 : ")
#
#     if user_input.lower() == "z":
#         break
#
#     print_times_table(int(user_input))

    # test
#
# A. UP DOWN 게임
# random 함수로 값을 초기화하고
# 사용자가 맞추는 게임
# result 가 50 인데 사용자가 36을 입력했다면 UP
# result 가 50인데 사용자가 70을 입력했다면 DOWN
# 성공했을때 함수가 종료.
#
# * 성공의 기준
# - 사용자가 답안을 맞춰야함. (필수)
# + 5번 이내에 맞추는것 (선택)
import random

def updown():
    result = random.randrange(1, 100)
    while True:
        user_input = int(input("값을 입력하세요 : "))
        if user_input == result:
            print("정답입니다.")
            break
        else:
            if user_input < result:
                print("up")
            else:
                print("down")
updown()


# B : 영어 단B. 영어 단어 퀴즈
# 자체 Dictionary 를 만들어서 random으로 문제가 출제되게
# 영어 기준 혹은 한글 기준 출력이 되면 사용자가 맞추는 형태
# 10번 출제
# 주관식 / 객관식 랜덤 (선택) - 기본만 하시는 경우 주관식만
# - 주관식 "Apple" 사용자가 "사과" 10점이 추가 (필수)
# - 객관식 "Apple" (선택)
# 1. 사과
# 2. 바나나
# 3. 포도
# 4. 멜론
# 번호가 맞을때 10점이 추가