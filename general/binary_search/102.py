def main(n, a, b, w, h):
    left, right = 0, max(w, h) // 2

    def check(d):
        return max(((w // (a + 2 * d)) * (h // (b + 2 * d)), ((w // (b + 2 * d)) * (h // (a + 2 * d))))) >= n

    while left < right:
        m = (left + right + 1) // 2
        if check(m):
            left = m
        else:
            right = m - 1
    return left


if __name__ == '__main__':
    n1, a1, b1, w1, h1 = map(int, input().split())
    print(main(n1, a1, b1, w1, h1))
