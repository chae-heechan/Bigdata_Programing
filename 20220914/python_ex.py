from datetime import datetime, date, time
import bisect
import re


def main():

    tup = 4, 5, 6       # 튜플 선언
    print(tup)

    n_tup = (4, 5, 6), (7, 8)
    print(n_tup)

    l = [4, 0, 2]       # 리스트 선언
    print(l)
    tup = tuple(l)      # 리스트 to 튜플
    print(tup)
    print(tup[0])

    tup = tuple(["foo", [1, 2], True])      # 튜플 선언
    print(tup)
    # tup[2] = False        # 튜플은 item변경이 불가능
    tup[1].append(3)        # 삽입은 가능
    print(tup)

    tup = (4, 5, 6)
    a, b, c = tup           # 하나씩 대입
    print(b)
    print(c)

    a_list = [2, 3, 7, None]
    tup = ("foo", "bar", "baz")
    print(a_list)   # 리스트는 []
    print(tup)      # 튜플은 ()

    b_list = list(tup)  # 튜플 to 리스트
    print(b_list)
    b_list[1] = "test"  # 1번 인덱스의 값 test로 변경
    print(b_list)

    b_list.append("dwarf")  # 리스트 뒤에 dwarf 추가
    b_list.insert(2, "red")  # 2번 인덱스에 red 추가
    print("dwarf" in b_list)
    print("dwarf" not in b_list)

    a = [7, 2, 5, 1, 3]
    a.sort()        # 리스트 정렬
    print(a)
    b = ["saw", "small", "He", "foxes", "six"]
    b.sort(key=len)  # 리스트 길이 순으로 정렬
    print(b)

    c = [1, 2, 2, 2, 3, 4, 7]
    ret = bisect.bisect(c, 5)   # 이진 분할
    print(ret)
    bisect.insort(c, 6)  # 이진 분할
    print(c)

    seq = [7, 2, 3, 7, 5, 6, 0, 1]
    print(seq[1:5])     # 슬라이싱
    seq[3:4] = [6, 3]   # 3자리에  6, 3대입
    print(seq)
    print(seq[:5])  # 4까지 출력
    print(seq[3:])  # 3부터 출력
    print(seq[-4:])  # 뒤에서부터 4부터
    print(seq[-6:-2])   # 뒤에서부터 6부터 2까지

    some_list = ["foo", "bar", "baz"]   # 리스트 선언
    mapping = {}
    for i, v in enumerate(some_list):   # i에는 인덱스, v에는 값 넣고 반복
        mapping[v] = i
    print(mapping)

    l = sorted([7, 1, 2, 6, 0, 3, 2])   # 정렬해서  l에 대입
    print(l)

    seq1 = ["foo", "bar", "baz"]
    seq2 = ["one", "two", "three"]
    zipped = zip(seq1, seq2)        # 두 리스트 묶기
    print(list(zipped))

    l = list(reversed(range(10)))   # 숫자 뒤집에서 리스트로 만들어 l에 대입
    print(l)

    d1 = {'a': 'some_value', 'b': [1, 2, 3, 4]}  # 딕셔너리 선언
    print(d1)

    d1[7] = 'an integer'    # 키: 7, 값: an integer
    d1[5] = 'some value'    # 키: 5, 값, some value
    print(d1)
    del d1[5]               # 키가 5인 값 지우기
    print(d1)
    d1.pop('b')             # 키가 b인 값 지우고 리턴
    print(d1)

    d1 = {'a': 'some value', 7: 'an integer'}
    d1.update({'b': 'foo', 'c': 12})        # 딕셔너리에 추가
    print(d1)

    key_list = ['a', 'b', 'c']
    value_list = ["foo", "bar", "baz"]
    mapping = {}
    for key, value in zip(key_list, value_list):    # 키, 리스트 하나씩 넣고 반복
        mapping[key] = value
    print(mapping)

    default = "default"
    some_dict = {'a': 'some value', 7: 'an integer'}
    value = some_dict.get('a', default)  # some_dict에서 a의 값 get
    print(value)

    s = set([2, 2, 2, 1, 3, 3])     # 중복 제거
    print(s)
    s = {2, 2, 2, 1, 3, 3}
    print(s)

    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}

    # a | b
    s = a.union(b)  # 합집합
    print(s)
    # a & b
    s = a.intersection(b)   # 교지합
    print(s)
    # a - b
    s = a.difference(b)     # 차집합
    print(s)

    def my_func(x, y, z=1.5):       # z입력이 없을 경우 디폴트값 1.5
        if z > 1:
            return z*(x+y)
        else:
            return z/(x+y)
    ret = my_func(4, 6, 3.5)
    print(ret)
    ret = my_func(10, 20)
    print(ret)
    ret = my_func(10, 20, -1)
    print(ret)

    def func():     # 01234 넣기
        a = []
        for j in range(5):
            a.append(j)
        print(a)

    func()

    b = []

    def func2():       # 01234 넣기
        for j in range(5):
            b.append(j)
        print(b)

    func2()

    c = None

    def func3():    # 01234 넣기
        global c
        c = []
        for j in range(5):
            c.append(j)
        print(c)

    func3()

    def f():
        a = 5
        b = 6
        c = 7
        return a, b, c  # 한번에 여러값 리턴

    l, m, n = f()   # 한번에 여러값 대입
    print(l, m, n)

    states = ['Alabama', 'Georgia!', 'Georgia', 'georgia',
              'FlOriDa', 'south carolina##', 'West virginia?']

    def clean_str(strings):
        ret = []
        for value in strings:
            value = value.strip()
            value = re.sub('[!#?]', '', value)  # 정규식 사용
            value = value.title()
            ret.append(value)
        return ret

    s = clean_str(states)   # 값 정리 후 대입
    print(s)

    def short_func(x):  # 곱하기 2
        return x*2

    z = 2
    ret1 = short_func(z)    # z*2
    ret2 = (lambda x: x*2)(z)   # z*2
    print(ret1, ret2)

    def attempt_float(x):
        try:                    # 자바의 try-chatch와 같음
            return float(x)
        except ValueError:  # valueerror가 뜰 경우
            return x

    ret = attempt_float('1.23')
    print(ret)
    ret = attempt_float('something')
    print(ret)


if __name__ == '__main__':  # main()
    main()
