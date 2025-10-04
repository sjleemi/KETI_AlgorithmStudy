# 백준 2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.


def find_max_index():
    n = list(map(int, input().split()))
    max = n[0]
    index = 0

    for i in range(1, 9):
        if n[i] > max:
            max = n[i]
            index = i

    return (max, index + 1)


def find_max_index2():
    num_list = []

    # 9개 자연수를 한 줄씩 입력받아 리스트에 추가
    for i in range(9):
        input_num = int(input())
        num_list.append(input_num)
    #append가 메모리상에서 어떻게 일어나는지 알아보기

    max = num_list[0]
    index = 0

    # 1번째부터 마지막까지 비교
    for i in range(1, 9):
        if num_list[i] > max:
            max = num_list[i]
            index = i

    # 몇 번째 수인지 출력해야 하니까 +1
    return (max, index + 1)


#실행
m, idx = find_max_index2()
print(m)
print(idx)

m,idx = find_max_index()
print(m)
print(idx)
