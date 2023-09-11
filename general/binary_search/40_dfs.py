def main(n, graph):
    distances_in_square = set()
    for neighbors in graph:
        for neighbor in neighbors:
            distances_in_square.add(neighbor[1])
    distances_in_square = sorted(distances_in_square)

    def check(r):
        colors = {vx: 0 for vx in range(n)}
        for start in range(n):
            if colors[start] != 0:
                continue
            stack = [start]
            colors[start] = 1
            while stack:
                cur_vertex = stack.pop()

                for neighbor in graph[cur_vertex]:
                    node, dist = neighbor[0], neighbor[1]
                    if dist < r:
                        if colors[node] == 0:
                            colors[node] = 3 - colors[cur_vertex]
                            stack.append(node)
                        elif colors[node] == colors[cur_vertex]:
                            return False
        return True, colors
    left, right = 0, len(distances_in_square) - 1
    while left < right:
        m = (left + right + 1) // 2
        if check(distances_in_square[m]):
            left = m
        else:
            right = m - 1
    return distances_in_square[left] ** (1/2)/2, list(check(distances_in_square[left])[1].values())


if __name__ == '__main__':
    n1 = int(input())
    coordinates1 = []
    for _ in range(n1):
        coordinates1.append(list(map(int, input().split())))
    graph1 = [
        [
            [
                vx, (cur_xy[0] - xy[0]) ** 2 + (cur_xy[1] - xy[1]) ** 2
            ] for vx, xy in enumerate(coordinates1) if vx != cur_vx
        ] for cur_vx, cur_xy in enumerate(coordinates1)
    ]
    r, colors = main(n1, graph1)
    print(r)
    print(*colors)
