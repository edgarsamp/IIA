from graph import *
import queue as Q

def calc_cost(cost, grafo, current, neighbor):
    return cost + grafo[current][neighbor]

def uniform_cost(graph, start, end):
    if not start in graph or not end in graph:
        return None, -1

    q = Q.PriorityQueue()
    q.put((0, [start]))
    
    while not q.empty():
        teste = q.queue
        node = q.get()
        cost = node[0]
        path = node[1]
        current = path[-1]
        
        if current == end:
            return path, cost
        
        for neighbor in graph[current]:
            if neighbor in path:
                continue
            temp = path.copy()
            temp.append(neighbor)
            temp_cost = calc_cost(cost, graph, current, neighbor)

            q.put((temp_cost, temp))
            
    return None, -1

print(uniform_cost(graph, 'Arad', 'Bucharest'))