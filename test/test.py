def main():
    answer = 0
    sum_num = 0
    i, j = 0, 0
    a, b = input().split(" ")
    a, b = int(a), int(b)

    while True:
        if sum_num + i >= a:    # 다음 값을 더하면 a보다 커지면
            break

        sum_num += i
        i += 1

    count_a = a - sum_num - 1       # 앞에 더해야 하는 남은 수
    sum_num = 0

    while True:
        if sum_num + j >= b:    # 다음 값을 더하면 b보다 커지면
            break

        sum_num += j
        j += 1

    count_b = b - sum_num

    if i == j:
        answer += (count_b - count_a) * i
    if i != j:
        answer += count_a * i
        answer += count_b * j
        for k in range(i+1, j):
            answer += k * k

    print(answer)


main()
