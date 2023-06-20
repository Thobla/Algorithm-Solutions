#Plan:
# 1: Topological sortingto find best "itteration-path"

from collections import deque
inp = input().split()

n_nodes = int(inp[0])
n_edges = int(inp[1])



out_edges = {}
in_edges = {}

for i in range(n_nodes): 
    
    out_edges[i+1] = []
    in_edges[i + 1] = None


for i in range(n_edges):
    inp = input().split()
    start = int(inp[0])
    end = int(inp[1])

    if len(out_edges[start]) == 0:
        out_edges[start] = [end]
    else:
        out_edges[start].append(end)


    if in_edges[end] == None:
        in_edges[end] = [start]
    else:
        in_edges[end].append(start)
    
    




in_path_1 = [False] * (n_nodes + 1)
in_path_2 = [False] * (n_nodes + 1)

in_path_1[1] = True
d_que = deque()
d_que.append(1)
while len(d_que) > 0:
    node = d_que.popleft()
    if not out_edges[node] == None:
        for elem in out_edges[node]:
            if not in_path_1[elem]:
                in_path_1[elem] = True
                d_que.appendleft(elem)


in_path_2[2] = True
d_que.append(2)
while len(d_que) > 0:
    node = d_que.popleft()
    if not in_edges[node] == None:
        for elem in in_edges[node]:
            if in_path_1[elem] and not in_path_2[elem]: #if we have reached it through 1, we add it to the path
                in_path_2[elem] = True
                d_que.appendleft(elem)




nodes_in_path = []
for i in range(n_nodes + 1):
    if in_path_2[i]:
        nodes_in_path.append(i)

in_count = [0] * (n_nodes + 1)

def update_out_edges(): #replaces the out edges and also updates the in_count
    new_out_edges = {}
    for i in range(n_nodes):
        new_out_edges[i + 1] = []


    for elem in out_edges:
        if in_path_2[elem]:
            for elem_2 in out_edges[elem]:
                if in_path_2[elem_2]:
                    in_count[elem_2] += 1
                    new_out_edges[elem].append(elem_2)
    return new_out_edges
       
out_edges = update_out_edges()

value_count = [0] * (n_nodes + 1)
value_count[1] = 1

def top_sort():
    d_queue = deque()

    visited = 0

    if in_count[1] == 0:
        d_queue.append(1)

    result = []

    while len(d_queue) > 0:
        visited += 1
        node = d_queue.popleft()
        result.append(node) #add to the sorted list
        if not out_edges[node] == None:
            for elem in out_edges[node]:
                if not elem == None:
                    in_count[elem] -= 1
                    if in_count[elem] == 0:
                        d_queue.append(elem) #appending to the queue as it's incoming edges are now zero

    return result


topo = top_sort()

for elem in topo:
    if not out_edges[elem] == None:
        for j in out_edges[elem]:
            value_count[j] += value_count[elem]

if len(topo) < len(nodes_in_path): #we have a cycle in the path
    print("inf")
else:
    new_str = str(value_count[2])
    if len(new_str) >= 10:
        final = ""
        for i in range(9):
            final =  new_str[-(i + 1)] + final
        print(final) #YOOOOOOOOOO, DET FUNKER JO!
    else:
        print(new_str)


