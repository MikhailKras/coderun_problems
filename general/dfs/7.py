def main(graph):
    start_vertex = 1
    stack = [start_vertex]
    visited = set()
    while stack:
        cur_vertex = stack.pop()
        if cur_vertex in visited:
            continue
        visited.add(cur_vertex)
        for neighbor in graph[cur_vertex]:
            stack.append(neighbor)

    return len(visited), sorted(visited)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        first, second = map(int, input().split())
        adj_list[first].append(second)
        adj_list[second].append(first)
    len_component, component = main(adj_list)
    print(len_component)
    print(*component)
