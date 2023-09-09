def main(n, x, y):
    left, right = 1, n * max(x, y)

    def check(num):
        min_xy = min(x, y)
        return 1 + (num - min_xy) // x + (num - min_xy) // y >= n

    while left < right:
        m = (left + right) // 2
        if check(m):
            right = m
        else:
            left = m + 1
    return left


if __name__ == '__main__':
    n1, x1, y1 = map(int, input().split())
    print(main(n1, x1, y1))
