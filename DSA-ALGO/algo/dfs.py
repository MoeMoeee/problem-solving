

def dfs (graph, start):
    visited = [] # list keeping track of the visited nodes
    result = []
    


if __name__ == '__main__':
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    print(dfs(graph, 0))