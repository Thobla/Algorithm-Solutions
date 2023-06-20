inp = input().split()
n_nodes = int(inp[0])
m_edges = int(inp[1])
c_colors = int(inp[2])

adj_list = []
color_dict = {}
inp = input().split()
for i in range(n_nodes):
    adj_list.append([])
    color_dict[i] = 2**(int(inp[i]) - 1) #colors goes from 0 and up, node names goes from 0 and up


for _ in range(m_edges):
    inp = input().split()
    a = int(inp[0]) - 1
    b = int(inp[1]) - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

meme = [] #memorization table remembering which colors have found the paths
for _ in range(n_nodes):
    meme.append({})
count = 0

def find_paths(node, color_mask, loc_count):
    local_count = loc_count 
    for neighbour in adj_list[node]:
        if not (color_mask & color_dict[neighbour]) > 0: #if we need the color
            if color_mask in meme[neighbour]:
                local_count += meme[neighbour][color_mask] # +1 ?

            else:
                new_color_mask = color_mask | color_dict[neighbour]
                meme[neighbour][color_mask] = find_paths(neighbour, new_color_mask, loc_count) + 1
                local_count += meme[neighbour][color_mask]

    return local_count

for i in range(n_nodes):
    count += find_paths(i, color_dict[i], 0)

print(count)

