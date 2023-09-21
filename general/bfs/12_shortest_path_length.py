from collections import deque


def main(graph, start, end, n):
    start, end = start - 1, end - 1
    queue = deque([start])
    visited = [-1] * n
    visited[start] = 0
    while queue:
        cur_node = queue.popleft()
        if cur_node == end:
            return visited[end]
        for neighbor, is_edge in enumerate(graph[cur_node]):
            if is_edge and visited[neighbor] == -1:
                queue.append(neighbor)
                visited[neighbor] = visited[cur_node] + 1
    else:
        return -1


if __name__ == '__main__':
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    start, end = map(int, input().split())
    print(main(adj_matrix, start, end, n))
