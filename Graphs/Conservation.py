test_cases = int(input())
from collections import deque

results = []
for i in range(test_cases):
    inp = input().split()
    stages = int(inp[0])
    dependencies = int(inp[1])
    lab_list = []
    
    
    for elem in input().split():
        lab_list.append(int(elem))

    original_in_edges = [0] * stages
    original_adj_list = []
    for j in range(stages):
            original_adj_list.append([])

    for j in range(dependencies):
            inp = input().split()
            dependent = int(inp[0]) - 1 #PS! making the input go from 0 to n-1 instead of 1 to n
            depender = int(inp[1]) - 1 #PS!

            original_adj_list[dependent].append(depender)
            original_in_edges[depender] += 1



    curr_result = []
    for lab in range(1, 3):



        if lab == 1:
            adj_list = original_adj_list.copy()
            in_edges = original_in_edges.copy()
        else:
            adj_list = original_adj_list
            in_edges = original_in_edges
        
    
        
    
    
        stage_count = stages
        transport_count = 0 #amount of times bitalisa has been transfered
        current_lab = lab
        next_non_dependency_list = deque([])
        while stage_count  >  0: # n
           
            non_dependency_list = deque([])
            if not len(next_non_dependency_list) == 0:
                non_dependency_list = next_non_dependency_list.copy()
                next_non_dependency_list = deque([])
            else:
                next_non_dependency_list = deque([])
                k = 0
                for elem in in_edges: # complexity - n
                    if elem == 0:
                        if lab_list[k] == current_lab:
                            non_dependency_list.append(k)
                        else:
                            next_non_dependency_list.append(k)
                    k += 1
            
        
            while len(non_dependency_list) > 0:
                    
                in_edges[non_dependency_list[0]] = None
                stage_count -= 1 #decrease the stage_count cause we now finished a stage

                for elem in adj_list[non_dependency_list[0]]:
                    in_edges[elem] -= 1
                    
                    if in_edges[elem] == 0:
                        if lab_list[elem] == current_lab:
                            non_dependency_list.append(elem) #since one of their dependencies was finished, we might be able to finish
                        else:
                            next_non_dependency_list.append(elem)
                non_dependency_list.popleft()


         
            if current_lab == 1 and stage_count > 0:
                current_lab = 2
                transport_count += 1
            elif current_lab == 2 and stage_count > 0:
                current_lab = 1
                transport_count += 1
            
        curr_result.append(transport_count)
    results.append(min(curr_result))
for elem in results:
    print(elem)
        

                
            





