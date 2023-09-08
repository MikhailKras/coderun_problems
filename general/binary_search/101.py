def main(w, h, n):
    left, right = 0, max(w, h) * n

    while left < right:
        m = (left + right) // 2
        if (m // w) * (m // h) >= n:
            right = m
        else:
            left = m + 1
    return left


if __name__ == '__main__':
    w1, h1, n1 = map(int, input().split())
    print(main(w1, h1, n1))
