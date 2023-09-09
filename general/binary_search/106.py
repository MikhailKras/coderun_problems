def main(n, k, l_list):
    left, right = 0, max(l_list)

    def check(len_test):
        return sum(map(lambda x: x // len_test, l_list)) >= k

    while left < right:
        m = (left + right + 1) // 2
        if check(m):
            left = m
        else:
            right = m - 1
    return left


if __name__ == '__main__':
    n1, k1 = map(int, input().split())
    lst = []
    for _ in range(n1):
        lst.append(int(input()))
    print(main(n1, k1, lst))
    