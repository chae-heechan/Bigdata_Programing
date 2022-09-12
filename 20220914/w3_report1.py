def main():
  student_list = ['Olivia', 'Emma', 'Ava', 'Mia', 'Evelyn']
  longest_list = []
  max_len = 0

  for word in student_list:   # student_list 반복
    if max_len < len(word):   # word가 최대 길이보다 클 경우
      max_len = len(word)     # max_len에 해당 길이 저장

  for word in student_list:
    if max_len == len(word):  # 해당 word가 최대 길이일 경우
      longest_list.append(word) # word를 longest_list에 저장

  print("가장 길이가 긴 문자열 : ", end="")
  for word in longest_list:   # longest_list 반복
    print(word, end=" ")    # word 출력
    student_list.remove(word) # student_list에서 삭제
  
  print()
  print("student_list = ", end="")
  print(student_list)

main()
