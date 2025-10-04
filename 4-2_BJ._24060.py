# 24060 , 병합정렬, k 번째 수 출력
# RUNTIME ERR
# 참고: https://youtu.be/QAyl79dCO_k?si=XF1xkjoySKAteIQq



def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr


# 입력 받기
N, K = map(int, input().split())
arr = list(map(int, input().split()))


merge_sort(arr)
print(merge_sort(arr)[K-1])