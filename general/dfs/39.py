def main(graph):
    stack = [1]
    visited = set()
    while stack:
        cur_vx = stack.pop()
        if cur_vx in visited:
            continue
        visited.add(cur_vx)
        for neighbor in graph[cur_vx]:
            stack.append(neighbor)
    return sorted(visited)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        first, second = map(int, input().split())
        adj_list[second].append(first)
    print(*main(adj_list))
