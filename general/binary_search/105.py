def main(n, m, t):
    left, right = 0, max(n, m)

    def check(d):
        return n - 2 * d >= 0 and m - 2 * d >= 0 and n * m - (n - 2 * d) * (m - 2 * d) <= t

    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    n1 = int(input())
    m1 = int(input())
    t1 = int(input())
    print(main(n1, m1, t1))
