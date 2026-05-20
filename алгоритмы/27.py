def find_peak(A):
    left = 0
    right = len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] < A[mid + 1]:
            # идём вверх → пик справа
            left = mid + 1
        else:
            # идём вниз → пик слева или mid
            right = mid

    return left   # индекс пика

A = [1, 3, 7, 12, 90,35, 25,  100, 6, 5, 2, 13]

print("Пик:", A[find_peak(A)])