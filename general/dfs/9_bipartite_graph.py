def main(n, graph):
    visited = {vx: 0 for vx in range(1, n + 1)}
    for start_vx in visited:
        if visited[start_vx]:
            continue
        stack = [start_vx]
        visited[start_vx] = 1
        while stack:
            cur_vx = stack.pop()
            for neighbor in graph[cur_vx]:
                if visited[neighbor] == 0:
                    stack.append(neighbor)
                    visited[neighbor] = 3 - visited[cur_vx]
                elif visited[neighbor] == visited[cur_vx]:
                    return "NO"
    return "YES"


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        first, second = map(int, input().split())
        adj_list[first].append(second)
        adj_list[second].append(first)
    print(main(n, adj_list))
