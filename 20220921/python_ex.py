import numpy as np


def main():

    data = np.random.randn(2, 3)    # 난수로 2 * 3 array 생성
    print(data)
    print(data * 10)        # 각 item에 10 곱하기
    print(data + data)      # 각 item에 item 더하기

    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1)  # data의 값으로 array 생성
    print(arr1)
    print(arr1.ndim)    # 1차원
    print(arr1.shape)   # (5,)
    print(arr1.dtype)   # float

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)      # data의 값으로 2차원 array 생성
    print(arr2)
    print(arr2.ndim)    # 2차원
    print(arr2.shape)  # (2, 4)
    print(arr2.dtype)   # int

    arr3 = np.zeros((2, 3))     # 0으로 2 * 3 array 생성
    print(arr3)
    print(arr3.ndim)    # 2차원

    arr3 = np.ones((2, 3))      # 1로 2 * 3 array 생성
    print(arr3)
    print(arr3.ndim)    # 2차원

    arr4 = np.empty((2, 3))     # 빈 2 * 3 array 생성
    print(arr4)

    arr = np.arange(5)      # [0, 1, 2, 3, 4]
    print(arr)

    arr = np.array([[1., 2., 3.], [4., 5., 6.]])    # 2차원 array 생성
    print(arr)
    arr2 = arr * arr    # 각 item의 제곱
    print(arr2)

    arr2 = 1 / arr  # 1을 각 item으로 나눈 값
    print(arr2)

    arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
    val = arr2 > arr    # arr2의 해당값이 arr 보다 클 경우 True 작을 경우 False
    print(val)

    arr = np.arange(10)     # [0, 1, 2, ..., 9]
    print(arr)
    print(arr[5])           # 인덱싱
    print(arr[5:8])         # [5, 6, 7] 슬라이싱

    arr[5:8] = 12       # 5번부터 7번 인덱스까지 12 대입
    print(arr)

    arr[:] = 10     # 전체에 10 대입
    print(arr)

    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])     # 3 * 3 array 생성
    print(arr2d)
    print(arr2d[2])
    print(arr2d[0][2])
    print(arr2d[0, 2])

    # 2 * 2 * 3 array 생성
    arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr3d)
    print(arr3d[0])

    old = arr3d[0].copy()   # arr3d에서 0번째 value 복사
    print(old)
    print(arr3d[1, 0])     # el: 2nd, row: 0
    print(arr3d[1, 0, 2])  # el:2nd, row: 0, col: 2

    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will',
                     'Joe', 'Joe'])   # 이름 들어간 array 생성
    data = np.random.randn(7, 4)    # 랜덤한 값으로 초기화된 7 * 4 array 생성
    print(names)
    print(data)

    print(names == 'Bob')       # Bob과 일치할 경우 True 다를 경우 False
    print(data[names == 'Bob'])  # names에서 일치한 인덱스를 data에서 출력
    mask = (names == 'Bob') | (names == 'Will')  # Bob과 일치하거나 Will과 일치한 경우 mask
    print(mask)
    print(data[mask])   # mask의 값이 True인 인덱스를 data에서 출력

    arr = np.empty((8, 4))       # 빈 8 * 4 array 생성
    for i in range(8):
        arr[i] = i  # 0부터 7까지 array에 대입
    print(arr)
    print(arr[[4, 3, 0, 6]])    # arr[4], arr[3], arr[0], arr[6]

    # [0, 1, 2, 3, ..., 31, 32] 만든후 8 * 4 array로 변경
    arr = np.arange(32).reshape((8, 4))
    print(arr)
    # arr[1, 0], arr[5, 3], arr[7, 1], arr[2, 2]
    print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

    # [0, 1, 2, 3, ..., 14, 15] 만든 후 3 * 5 array로 변경
    arr = np.arange(15).reshape((3, 5))
    print(arr)
    print(arr.T)  # 5 * 3 으로 뒤집어서 출력

    arr = np.random.randn(6, 3)      # 빈 6 * 3 array 생성
    print(arr)
    val = np.dot(arr.T, arr)    # 3*6 * 6*3 -> 3*3
    print(val)

    arr = np.arange(10)  # [0, 1, 2, ..., 9]
    print(arr)
    val = np.sqrt(arr)  # 긱 item에 루트 씌우기
    print(val)
    val = np.exp(arr)   # 각 item을 지수함수로 변경 e^0, e^1
    print(val)

    x = np.random.randn(8)      # 난수 8개 array 생성
    y = np.random.randn(8)      # 난수 8개 array 생성
    print(x)
    print(y)
    val = np.maximum(x, y)      # 둘중 최대값 인 값  array
    print(val)

    arr = np.random.randn(7) * 5    # 난수 7개 * 5 array 생성
    print(arr)

    remainder, whole_part = np.modf(arr)
    print(whole_part)   # 정수부
    print(remainder)    # 나머지


if __name__ == '__main__':
    main()
