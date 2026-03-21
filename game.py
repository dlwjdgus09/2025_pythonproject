import random

weapon_level = 0
upgrade_rates = [
        #{"up": 80, "keep": 20, "down": 0, "break": 0},
        #{"up": 70, "keep": 20, "down": 5, "break": 5},
        #{"up": 60, "keep": 25, "down": 10, "break": 5},
        #{"up": 55, "keep": 25, "down": 15, "break": 5},
        #{"up": 45, "keep": 25, "down": 20, "break": 10},
        #{"up": 40, "keep": 30, "down": 20, "break": 10},
        #{"up": 35, "keep": 30, "down": 25, "break": 10},
        #{"up": 30, "keep": 30, "down": 25, "break": 15},
        #{"up": 20, "keep": 30, "down": 30, "break": 20},
        #{"up": 15, "keep": 30, "down": 30, "break": 25},
        #{"up": 0, "keep": 100, "down": 0, "break": 0}
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 100, "keep": 0, "down": 0, "break": 0},
        {"up": 0, "keep": 100, "down": 0, "break": 0}
    ]

def upgrade_weapon(current_lv):


    ran_num = random.randint(0, 99)
    rate = upgrade_rates[current_lv]
    print(rate)
    print(ran_num)
    if current_lv == 10:
        print("더 이상 업그레이드가 불가능합니다")
        return current_lv

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



    if 0 <= current_lv <= 10:
        if ran_num == "up":
            print("강화 시도 결과 :", ran_num, "성공!")
        elif ran_num == "keep" :
            print("강화 시도 결과 :", ran_num, "유지")
        elif ran_num == "down" :
            print("강화 시도 결과 :", ran_num, "하락")
        else :
            print("강화 시도 결과 :", ran_num, "파괴")
        print("현재 무기 레벨 :", current_lv)

    return current_lv

boss_level = 0
boss_names = ["슬라임", "좀비", "고블린", "스켈레톤", "오크", "골렘", "웨어울프", "뱀파이어", "히드라", "데몬", "드래곤"]



def start_battle(w_lv, b_lv):
    level_diff = w_lv - b_lv
    if level_diff <= -3:
        win_rate = 0
    elif level_diff == -2 :
        win_rate = 20
    elif level_diff == -1:
        win_rate = 30
    elif level_diff == 0:
        win_rate = 50
    elif level_diff == 1:
        win_rate = 70
    elif level_diff == 2:
        win_rate = 90
    else:
        win_rate = 100

    ran_num = random.randint(0, 99)
    print(level_diff)
    print(boss_names[b_lv])
    print(f"보스 레벨 :", boss_level)
    print(f"레벨 :", weapon_level)

    return ran_num < win_rate



def show_status():
    is_dragon_slayer = False
    if boss_level == 11:
        print("축하합니다! 모든 보스를 제압했습니다!")
        is_dragon_slayer = True
    if is_dragon_slayer:
        print("[드래곤 처치자] 전설의 용사님, 환영합니다!")
    return

print("게임에 오신 것을 환영합니다!")
while True:
    print("2. 보스 도전")
    print("1. 무기 강화")
    print("0. 종료하기")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료):")
    if choice == "0":
        print("게임을 종료합니다.")
        break
    elif choice == "1":
        weapon_level = upgrade_weapon(weapon_level)
    elif choice == "2":
        if boss_level == 11:
            print("[드래곤 처치자] 전설의 용사님, 환영합니다!")
            print("이미 최종 보스를 격파하셨습니다")
        else:
            result = start_battle(weapon_level, boss_level)
            if boss_level < 10:
                if result:
                    boss_level = boss_level + 1
                    print("보스 처치 성공!")
                else:
                    boss_level = boss_level
                    print("처참하게 패배했습니다...")

            else:
                if result:
                    boss_level = boss_level + 1
                    print("보스 처치 성공!")
                    show_status()
                else:
                    boss_level = boss_level
                    print("처참하게 패배했습니다...")

    else:
        print("잘못 입력하셨습니다")

