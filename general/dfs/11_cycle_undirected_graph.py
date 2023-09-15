def main(n, graph):
    visited = [{'visited': False, 'parent': -1} for _ in range(n)]
    vxs_in_cycle = []
    for start_vx in range(n):
        if visited[start_vx]['visited']:
            continue
        stack = [(start_vx, -1)]
        while stack:
            cur_vx, parent = stack.pop()
            if visited[cur_vx]['visited']:
                continue
            visited[cur_vx]['visited'], visited[cur_vx]['parent'] = True, parent
            for neighbor in range(n):
                if graph[cur_vx][neighbor] and neighbor != parent:
                    if visited[neighbor]['visited'] and visited[neighbor]['parent'] != cur_vx:  # cycle found
                        node = cur_vx
                        vxs_in_cycle.append(node)
                        while node != neighbor:
                            node = visited[node]['parent']
                            vxs_in_cycle.append(node)
                        return "YES", list(map(lambda x: x + 1, vxs_in_cycle))
                    stack.append((neighbor, cur_vx))
    return "NO"


if __name__ == '__main__':
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    ans = main(n, adj_matrix)
    if ans == "NO":
        print(ans)
    else:
        answer, cycle = ans[0], ans[1]
        print(answer)
        print(len(cycle))
        print(*cycle)
