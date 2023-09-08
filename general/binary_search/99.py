def main(n, k, a_list, b_list):
    def binary_search(num):
        left, right = 0, n - 1
        while left < right:
            m = (left + right) // 2
            if a_list[m] >= num:
                right = m
            else:
                left = m + 1
        return "NO" if a_list[left] != num else "YES"

    for i in b_list:
        print(binary_search(i))


if __name__ == '__main__':
    n1, k1 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    main(n1, k1, a, b)
