score = int(input("점수를 입력하세요."))
if score <= 100:
    if score >= 0:
        if score >= 80:
            print("합격입니다.")
        elif score >= 60:
            print("재시험 응시가 필요합니다.")
        else:
            print("불합격입니다.")