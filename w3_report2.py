def main():
  file = 'C:\채희찬\공부\Bigdata_Programing\height.txt'
  f = open(file, 'r') # 읽기 모드로 파일 열기

  height_list = []

  for line in f:
    name, height_s = line.split(" ")
    height = isNumber(height_s)

    if height:    # 두번쩨 단어가 숫자일 경우
      height_list.append(height)

    # 수동 방식
    #   if height >= first_place:  # 1등보다 크거나 같을 경우
    #     third_place = second_place
    #     second_place = first_place
    #     first_place = height
    #   else: # 1등보다 작을 경우
    #     if height >= second_place:  # 2등보다 크거나 같을 경우
    #       third_place = second_place
    #       second_place = height
    #     else: # 2등보다 작을 경우
    #       if height > third_place:  # 3등보다 클 경우
    #         third_place = height
  
  for i in range(1, 4):   # 1,2,3 반복
    print(str(i) + "등: ", end="")
    print(max(height_list))   # 최댓값 출력 
    height_list.remove(max(height_list))  # 최댓값 삭제

  f.close() # 파일 닫기

def isNumber(num):  # 실수 판별 메서드
  try:
    float(num)    # float형으로 형변환
    return float(num)
  except ValueError:  # value error 시 False 리턴
    return False
  
main()