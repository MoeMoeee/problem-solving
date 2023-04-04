

def bfs(graph, start):
    visited = [] # list keeping track of the visited nodes
    result = []
    visited.append(start)
    result.append(start)
    
    while result:
        node = result.pop()
        for neighbor in graph[node]:
            # visited.append(node)
            if neighbor not in visited:
                visited.append(neighbor)
                result.append(neighbor)
                
    return visited


if __name__ == '__main__':
    graph = {
        0: [1, 2, 3],
        1: [0],
        2: [0, 3, 4],
        3: [0, 2],
        4: [2]
    }
    print(bfs(graph, 0))