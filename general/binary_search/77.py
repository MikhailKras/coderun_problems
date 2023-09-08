def main(a, b, c):
    left, right = 0, a + b + c

    def check(test_m):
        return (2 * a + 3 * b + 4 * c + 5 * test_m) >= 3.5 * (a + b + c + test_m)

    while left < right:
        m = (left + right) // 2
        if check(m):
            right = m
        else:
            left = m + 1
    return left


if __name__ == '__main__':
    a1 = int(input())
    b1 = int(input())
    c1 = int(input())
    print(main(a1, b1, c1))
