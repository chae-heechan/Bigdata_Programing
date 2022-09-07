def main():
    i = 0
    while True:
        if str(i)[-1] != "3":   # 마지막 자리가 3이 아닐 경우
            i += 1
            if i > 73:  # i가 73 초과일 경우
                break
        else:
            print(i, end=' ')
            i += 1


main()
