from datetime import datetime, date, time
import bisect


def main():

    a = [1, 2, 3]       # list로 선언
    print(a)
    b = a               # b에 a를 대입
    print(b)

    num = 5             # int로 선언
    print(type(num))

    ch = "foo"          # str로 선언
    print(type(ch))

    a = 2
    b = 5
    print(a*5)          # 일반 곱하기 연산
    print(a**5)         # 제곱 연산
    print(b//a)         # 몫만 나누기 연산

    alist = ["foo", 2, [4, 5]]      # 여러 자료형이 들어있는 list 선언
    print(alist)
    alist[2] = (3, 4)   # 2번 인덱스 값 변경
    print(alist)

    atuple = (3, 4, (4, 5))     # 튜플 생성
    print(atuple)
    #atuple[1] = "four"

    ival = 12345    # int형 변수 선언
    fval = 3.1415   # float형 변수 선언
    print(3/2)
    print(3//2)

    s = "python"    # string 선언
    print(s)
    l = list(s)     # string to list
    print(l)
    print(s[:3])    # string 슬라이싱
    print(l[:3])    # list 슬라이싱

    a = "hello, "
    b = "python"
    print(a + b)    # +연산자로 문자열 결헙

    # format 사용
    template = "{0:.2f} {1:s} are worth US$ {2:d}"
    t = template.format(4.5560, "Argentine Pesos", 1)
    print(t)

    val = "korean"
    val_utf8 = val.encode("utf-8")      # utf-8로 인코딩
    print(type(val_utf8))
    print(val_utf8.decode("utf-8"))     # utf-8로 디코딩 후 출력

    s = "3.14159"       # str형 변수 선언
    fval = float(s)     # str to float
    print(type(fval))
    print(type(int(fval)))

    s = None
    print(s is None)    # True

    # datetime 라이브러리 사용
    dt = datetime(2021, 3, 10, 15, 11, 30)
    print(dt.day)
    print(dt.minute)
    t = dt.strftime("%m/%d/%Y %H:%M")
    print(t)

    # 분기문(if, elif, else) 사용
    x = 10
    if x < 0:
        print("negative")
    elif x == 0:
        print("equal")
    elif 0 < x < 5:     # == 0 < x and x < 5
        print("positive but small")
    else:
        print("positive and large")

    a = 1
    b = 2
    c = 3
    d = 4
    if a < b or c > d:  # or을 이용한 두개의 조건 분기
        print("good job")
    else:
        print("not good")

    if a < b and c > d:  # and를 이용한 두개의 조건 분기
        print("good job")
    else:
        print("not good")

    sequence = [1, 3, None, 7, None, 11]
    total = 0
    for value in sequence:      # sequance의 값을 순서대로 하나씩 value에 넣고 반복
        if value is None:       # value가 None일 경우
            continue        # 아래는 생략 후 반복문 진행
        total += value      # None이 아닐 경우 total에 value 추가
    print(total)

    sequence = [1, 2, 3, 4, 5, 6, 7, 8]
    total = 0
    for value in sequence:
        if value == 5:      # value가 5가 나올때 까지 1 부터 더하기
            break           # 5면 멈춤
        total += value
    print(total)

    for j in range(10):     # range를 이용해 0 부터 9까지 반복
        print(j)

    x = 1
    while x < 10:   # x가 10 미만일 경우 반복
        total += x
        x += 1
    print(total)

    x = 1
    while x < 100:  # x가 100 미만일 경우 반복
        total += x
        if total > 50:  # 합이 50 초과일 경우 멈춤
            break
        x += 1
    print(total)

    # --------------------
    if x < 0:
        print("less position")
    elif x == 1:
        pass    # 아무일 없지만 명사해 두고 싶을때 pass 사용
    else:
        print("greater position")
    # --------------------

    x = 10
    ret = "Small-number" if x <= 100 else "Big-number"  # 삼항 표현
    print(ret)


if __name__ == '__main__':
    main()  # 메인 메서드 실행
