inp_data = input().split()
metals_count = int(inp_data[0])
experiments_count = int(inp_data[1])
sorted_list = []

adj_list = [0] * metals_count #Showing the nodes that the given node points to
in_edges = [0] * metals_count #Showing how many edges points to the given node

#makes adjecency list consist of empty lists
for i in range(len(adj_list)):
    adj_list[i] = []

#adds the edges to the adjecency list to the appropriate metal
for i in range(experiments_count):
    inp = input().split()
    high_react = int(inp[0])
    low_react = int(inp[1])

    adj_list[high_react].append(low_react)
    in_edges[low_react] += 1 #increments the low_react by 1 to show that there is 1 node that is bigger



def sort():
    
    while(1):
        highest_react = []

        i = 0
        for elem in in_edges:
            if elem == 0:
                highest_react.append(i)
            i += 1

        if len(highest_react) == 0:
            if len(sorted_list) < metals_count: #it is circular and we need to go back to the lab
                return "back to the lab"

        sorted_list.append(highest_react[0])
        in_edges[highest_react[0]] = None #we will not use it again
        for elem in adj_list[highest_react[0]]:
            in_edges[elem] -= 1 #removing one in_edge from the nodes that the original node was pointing to


        if len(sorted_list) >= metals_count:
                    return sorted_list
        
        elif len(highest_react) > 1: #there are several nodes with potentially highest reactivity, needs to be a unique series
            return "back to the lab"
        
        
        
        
        
    

result = sort()
if result == "back to the lab":
    print(result)
else:
    result_as_string = ""
    for elem in result:
        result_as_string += str(elem) + " "
    #result_as_string.strip()

    print(result_as_string)