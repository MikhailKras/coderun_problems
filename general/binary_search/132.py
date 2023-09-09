def main(n, diego_list, k, card_list):
    diego_list = sorted(set(diego_list))

    def binary_search(card):
        if card <= diego_list[0]:
            return 0

        left, right = 0, len(diego_list) - 1

        while left < right:
            m = (left + right + 1) // 2
            if diego_list[m] < card:
                left = m
            else:
                right = m - 1
        return left + 1

    for i in range(k):
        print(binary_search(card_list[i]))


if __name__ == '__main__':
    n1 = int(input())
    diego_list1 = list(map(int, input().split()))
    k1 = int(input())
    card_list1 = list(map(int, input().split()))
    main(n1, diego_list1, k1, card_list1)
