import math
from collections import deque
result = ""
line = 0
while True:
    try:
        inp = input().split()
        line += 1
        n_gophers = int(inp[0])
        m_holes = int(inp[1])
        time_limit = int(inp[2])
        velocity = int(inp[3])

        gophers_pos = []
        holes_pos = []

        for _ in range(n_gophers):
            line += 1
            inp = input().split()
            x_pos = float(inp[0])
            y_pos = float(inp[1])
            gophers_pos.append((x_pos, y_pos))

        for _ in range(m_holes):
            line += 1
            inp = input().split()
            x_pos = float(inp[0])
            y_pos = float(inp[1])
            holes_pos.append((x_pos, y_pos))


        adj_list = []
        cap_list = []

        gophers = []
        holes = []


        for _ in range(n_gophers + m_holes + 2):
            adj_list.append([])
            cap_list.append({})

        for i in range(1, n_gophers + 1):
            adj_list[0].append(i)
            adj_list[i].append(0)
            cap_list[0][i] = [0, 1]
            cap_list[i][0] = [0, 0]

        for i in range(n_gophers):
            for j in range(m_holes):
                time = math.sqrt((abs(gophers_pos[i][0] - holes_pos[j][0])) ** 2 + (abs(gophers_pos[i][1] - holes_pos[j][1])) ** 2)/velocity
                if time <= time_limit: #Think its correct to put <=?
                    adj_list[i + 1].append(n_gophers + 1 + j)
                    adj_list[n_gophers + 1 + j].append(i + 1)
                    cap_list[i + 1][n_gophers + 1 + j] = [0, 1]
                    cap_list[n_gophers + 1 + j][i + 1] = [0, 0] #residual graph i guess


        for i in range(n_gophers + 1, n_gophers + 1 + m_holes):
            adj_list[i].append(n_gophers + m_holes + 1)
            adj_list[n_gophers + m_holes + 1].append(i)
            cap_list[i][n_gophers + m_holes + 1] = [0, 1]
            cap_list[n_gophers + m_holes + 1][i] = [0, 0]



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
        
        print(n_gophers - flow)
    except EOFError:
        
        #print(result[:-1])
        break