# This solution only works on PyPy

def main(n, m, field):

    def get_neighbors(x, y):
        return list(filter(
            lambda item: 0 <= item[0] < n and 0 <= item[1] < m and field[item[0]][item[1]] <= field[x][y],
            [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        ))

    adj_list = [[] for _ in range(n * m)]

    for r in range(n):
        for c in range(m):
            neighbors = list(map(lambda item: item[0] * m + item[1], get_neighbors(r, c)))
            adj_list[r * m + c].extend(neighbors)

    visited = set()
    merged_vertexes = []
    for start in range(n * m):
        if start in visited:
            continue
        stack = [start]
        new_vx = [start]
        while stack:
            cur_vx = stack.pop()
            if cur_vx in visited:
                continue
            visited.add(cur_vx)
            for neighbor in adj_list[cur_vx]:
                if cur_vx in adj_list[neighbor] and neighbor not in visited:
                    new_vx.append(neighbor)
                    stack.append(neighbor)
        merged_vertexes.append(new_vx)

    counter = 0
    for vertexes in merged_vertexes:
        edges = 0
        for vx in vertexes:
            edges += len([edge for edge in adj_list[vx] if edge not in vertexes])
        if edges == 0:
            counter += 1
    return counter


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []
    for _ in range(n):
        field.append(list(map(int, input().split())))
    ans = main(n, m, field)
    print(ans)
