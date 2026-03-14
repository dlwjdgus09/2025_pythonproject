
import random

weapon_level = 0
upgrade_rates = [
        {"up": 70, "keep": 30, "down": 0, "break": 0},
        {"up": 60, "keep": 25, "down": 10, "break": 5},
        {"up": 50, "keep": 30, "down": 15, "break": 5},
        {"up": 45, "keep": 30, "down": 20, "break": 5},
        {"up": 40, "keep": 30, "down": 20, "break": 10},
        {"up": 35, "keep": 30, "down": 25, "break": 10},
        {"up": 30, "keep": 30, "down": 30, "break": 10},
        {"up": 25, "keep": 30, "down": 30, "break": 15},
        {"up": 20, "keep": 30, "down": 30, "break": 20},
        {"up": 15, "keep": 30, "down": 30, "break": 25},
        {"up": 0, "keep": 100, "down": 0, "break": 0}
    ]

def upgrade_weapon(current_lv):


    ran_num = random.randint(0, 99)
    rate = upgrade_rates[current_lv]
    if 1<= current_lv <=10:
        if ran_num < rate["up"]:
            ran_num = "up"
            current_lv = current_lv + 1
        elif rate["up"] <= ran_num < rate["up"] + rate["keep"]:
            ran_num = "keep"
            current_lv = current_lv
        elif rate["up"] + rate["keep"] <= ran_num < rate["up"] + rate["keep"] + rate["down"]:
            ran_num = "down"
            current_lv = current_lv - 1
        else:
            ran_num = "break"
            current_lv = 0
    elif current_lv == 0:
        if ran_num < rate["up"]:
            ran_num = "up"
            current_lv = current_lv + 1
        else :
            ran_num = "keep"
            current_lv = current_lv

    if 0 <= current_lv <= 9:
        if ran_num == "up":
            print("강화 시도 결과 :", ran_num, "성공!")
        elif ran_num == "keep" :
            print("강화 시도 결과 :", ran_num, "유지")
        elif ran_num == "down" :
            print("강화 시도 결과 :", ran_num, "하락")
        else :
            print("강화 시도 결과 :", ran_num, "파괴")
        print("현재 무기 레벨 :", current_lv)
    else :
        print("더 이상 업그레이드가 불가능합니다")

    return current_lv

print("게임에 오신 것을 환영합니다!")
while True:
    print("1. 무기 강화")
    print("0. 종료하기")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료):")
    if choice == "0":
        print("게임을 종료합니다.")
        break
    elif choice == "1":
        weapon_level = upgrade_weapon(weapon_level)
    else:
        break
