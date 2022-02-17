from graph import *

def calc_next_node(node):
    return min(graph[node].keys(), key= lambda x:d_bucharest[x])

def gulosa(graph, start, end):
    if not start in graph or not end in graph:
        return -1

    cost = 0
    path  = [start]
    node = start
    visited = set(node)

    while(node != end):
        next_node = calc_next_node(node)
        cost += graph[node][next_node]
        node = next_node
        path.append(node)

        if node in visited:
            return "Caminho não encontrado"
        else:
            visited.add(node)

    return (path, cost)


print(gulosa(graph, 'Arad', 'Bucharest'))
print(gulosa(graph, 'Arad', 'a'))
