def main():
    a_or_b = "참 잘했습니다."
    c_or_d = "좀더 노력하세요."
    f = "다음 학기에 다시 수강하세요."
    error_message = "잘못된 입력입니다."

    score = input()

    if score == "A" or score == "B":    # 학점이 A 또는 B일 경우
        print(a_or_b)
    elif score == "C" or score == "D":  # 학점이 C 또는 D일 경우
        print(c_or_d)
    elif score == "F":  # 학점이 F일 경우
        print(f)
    else:       # A~F 이외의 입력일 경우
        print(error_message)
        

main()
