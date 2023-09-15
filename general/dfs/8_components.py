def main(n, graph):
    visited = set()
    components = []
    for start_vertex in range(1, n + 1):
        if start_vertex in visited:
            continue
        stack = [start_vertex]
        component = set()
        while stack:
            cur_vertex = stack.pop()
            if cur_vertex in component:
                continue
            component.add(cur_vertex)
            for neighbor in graph[cur_vertex]:
                stack.append(neighbor)
                visited.add(neighbor)
        components.append(component)
    return components


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        first, second = map(int, input().split())
        adj_list[first].append(second)
        adj_list[second].append(first)
    components = main(n, adj_list)
    print(len(components))
    for component in components:
        print(len(component))
        print(*component)
