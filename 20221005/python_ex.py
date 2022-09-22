import pandas as pd
import numpy as np


def main():

    obj = pd.Series([4, 7, -5, 3])  # 시리즈로 배열 선언
    print(obj)

    print(obj.values)   # 값 출력
    print(obj.index)    # 인덱스 출력

    obj = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c']
                    )    # 인덱스를 d, b, a, c로 하는 시리즈 배열 선언
    print(obj)
    print(obj.index)

    obj = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c']
                    )    # 인덱스를 d, b, a, c로 하는 시리즈 배열 선언
    print(obj['a'])  # 인덱스 a 출력
    obj['d'] = 6    # 인덱스 d에 6 대입
    print(obj[['c', 'a', 'd']])   # 인덱스 c, a, d 출력

    obj = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c']
                    )    # 인덱스를 d, b, a, c로 하는 시리즈 배열 선언
    print(obj[obj > 0])     # 0초과값만 출력
    print(obj*2)        # 2곱해서 출력
    print(np.exp(obj))  # 지수로 출력

    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj = pd.Series(sdata)  # sdata를 시리즈로 변경
    print(obj)

    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj = pd.Series(sdata, index=states)    # 인덱스를 states로 하는 배열로 변경
    print(obj)

    val = pd.isnull(obj)    # 널값이 있는지
    print(val)
    val = pd.notnull(obj)   # 널값이 없는지
    print(val)

    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 'year': [
        2000, 2001, 2002, 2001, 2002, 2003], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)  # 테이블 방식의 데이터 프레임으로 선언
    print(frame)
    print(frame.head())     # 첫 5개 행만 출력

    # 행을 year state pop 으로 하는 데이터 프레임 선언
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
    print(frame)
    print(frame['state'])   # state만 출력

    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 'year': [
        2000, 2001, 2002, 2001, 2002, 2003], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=[
                         'one', 'two', 'three', 'four', 'five', 'six'])     # 행 열 정해주기
    print(frame)
    print(frame.loc['three'])       # three 만 출력

    frame['debt'] = np.arange(6)    # 새로 debt열 만들어서 0~5까지 넣어주기
    print(frame)
    # two four five에 -1.2, -1.5, -1.7 넣어주기
    val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    frame['debt'] = val  # 만들어둔 frame에 넣기
    print(frame)

    # eastern에 state가 Ohio면 True 아니면 False
    frame['eastern'] = (frame.state == 'Ohio')
    print(frame)

    del frame['debt']   # debt 삭제
    print(frame)

    # 0, 1, 2 에 인덱스 a, b, c 시리즈 배열 생성
    obj = pd.Series(range(3), index=['a', 'b', 'c'])
    index = obj.index   # index = a, b, c
    print(index)

    obj = pd.Series([4.5, 7.2, -5.3, 3.6],
                    index=['d', 'b', 'a', 'c'])  # 시리즈 배열로 선언
    print(obj)

    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])   # a, b, c, d, e 순으로 재색인
    print(obj2)

    # 0, 2, 4 번 인덱스에 blue, purple, yello값 넣기
    obj = pd.Series(['blue', 'purple', 'yello'], index=[0, 2, 4])
    # 0~5번까지 만들고 빈 값은 이전 값으로 채워 재색인
    obj3 = obj.reindex(range(6), method='ffill')
    print(obj3)

    # 9개를 3x3으로 만들고 행 a, c, d 열 Ohio, Texas, California로 데이터 프레임 생성
    frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=[
                         'a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
    print(frame)
    frame2 = frame.reindex(['a', 'b', 'c', 'd'])   # a, b, c, d로 재색인
    print(frame2)

    states = ['Texas', 'Utah', 'California']
    frame2 = frame.reindex(columns=states)  # Ohio 대신 Uath 넣고 재색인
    print(frame2)   # Utah 값은 NaN

    # 값 0.0 ~ 4.0 인덱스 a, b, c, d, e 배열 생성
    obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    print(obj)
    new = obj.drop('c')  # c삭제
    print(new)
    new = obj.drop(['d', 'c'])  # c, d 삭제
    print(new)

    data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=[
                        'Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])  # 4x4 배열 생성
    print(data)
    d1 = data.drop(['Colorado', 'Ohio'])  # colorado, ohio 삭제
    print(d1)
    d2 = data.drop('two', axis=1)   # two 삭제
    print(d2)


main()
