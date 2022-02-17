from graph import *
import queue as Q

def calc_path_cost(path):
    path_cost = 0
    for i in range(len(path)-1):
        path_cost += graph[path[i]][path[i+1]]

    return path_cost

def calc_cost(neighbor, path):
    global d_bucharest
    path_cost = calc_path_cost(path)

    return path_cost + d_bucharest[neighbor]

def a_start(graph, start, end):
    if not start in graph or not end in graph:
        return None, -1

    global d_bucharest
    q = Q.PriorityQueue()
    q.put((d_bucharest[start], [start]))
    
    while not q.empty():
        node = q.get()
        cost = node[0]
        path = node[1]
        current = path[-1]
        
        if current == end:
            return(path, cost)
        
        for neighbor in graph[current]:
            path_temp = path.copy()
            path_temp.append(neighbor)
            temp_cost = calc_cost(neighbor, path_temp)

            q.put((temp_cost, path_temp))
            
    return None, -1


print(a_start(graph, 'Arad', 'Bucharest'))