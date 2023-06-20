from collections import deque

inp = input().split()
n_children = int(inp[0])
m_toys = int(inp[1])
p_categories = int(inp[2])

child_preferences = {}
toys_in_category = {}
category_capacity = {}

toy_mentioned = [False] * (m_toys + 1)

for i in range(1, n_children + 1):
    child_preferences[i] = []
    inp = input().split()
    for j in range(1,int(inp[0]) + 1):
        child_preferences[i].append(n_children + int(inp[j]))

for i in range(p_categories):
    toys_in_category[i] = []
    inp = input().split()
    category_capacity[i] = int(inp[-1])
    for j in range(1, int(inp[0]) + 1):
        toys_in_category[i].append(n_children + int(inp[j]))
        toy_mentioned[int(inp[j])] = True

toys_in_category[p_categories] = []
category_capacity[p_categories] = float('inf')
for i in range(1, m_toys + 1):
    if toy_mentioned[i] == False:
        toys_in_category[p_categories].append(n_children + i)

adj_list = []
cap_list = []

for _ in range(n_children + m_toys + p_categories + 3):
    adj_list.append([])
    cap_list.append({})

for i in range(1, n_children + 1):
    adj_list[0].append(i)
    adj_list[i].append(0)
    cap_list[0][i] = [0, 1]
    cap_list[i][0] = [0, 0]
    for elem in child_preferences[i]:
        adj_list[i].append(elem)
        adj_list[elem].append(i)
        cap_list[i][elem] = [0, 1]
        cap_list[elem][i] = [0, 0]

for j in range(p_categories + 1):
    for toy in toys_in_category[j]:
        adj_list[toy].append(j + n_children + m_toys + 1)
        adj_list[j + n_children + m_toys + 1].append(toy)
        cap_list[toy][j + n_children + m_toys + 1] = [0, 1]
        cap_list[j + n_children + m_toys + 1][toy] = [0, 0]

    adj_list[j + n_children + m_toys + 1].append(len(adj_list) - 1)
    adj_list[len(adj_list) - 1].append(j + n_children + m_toys + 1)
    cap_list[j + n_children + m_toys + 1][len(adj_list) - 1] = [0, category_capacity[j]]
    cap_list[len(adj_list) - 1][j + n_children + m_toys + 1] = [0, 0]



def get_path():
    node = 0 #starts at source
    queue = deque([node])
    parent = {}
    while len(queue) > 0:
        node = queue.popleft()
        for elem in adj_list[node]:
            
            if (elem in parent) or (cap_list[node][elem][1] - cap_list[node][elem][0] <= 0):
                
                continue #we do not add because not a valid path
            else:
                parent[elem] = node
                queue.append(elem)
                if elem == len(adj_list) - 1: #we are at sink
                    path = [elem]
                    node = elem
                    while node != 0:
                        node = parent[node]
                        path.append(node)
                    return list(reversed(path))

flow = 0
while path := get_path():
    flow += 1
    for i in range(1, len(path)):
        start = path[i - 1]
        end = path[i]
        cap_list[start][end][0] += 1
        cap_list[end][start][0] -= 1


print(flow)


