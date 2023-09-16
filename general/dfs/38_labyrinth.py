def main(n, start_vx, labyrinth):
    start_row, start_col = start_vx[0] - 1, start_vx[1] - 1
    stack = [(start_row, start_col)]
    visited = set()
    square = 0

    def get_neighbors(r, c):
        return filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < n, [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        square += 1
        for neighbor in get_neighbors(row, col):
            if labyrinth[neighbor[0]][neighbor[1]] == "*":
                continue
            stack.append(neighbor)
    return square


if __name__ == '__main__':
    n = int(input())
    labyrinth = []
    for _ in range(n):
        labyrinth.append(list(input()))
    start = list(map(int, input().split()))
    print(main(n, start, labyrinth))
