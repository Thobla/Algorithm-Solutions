inp = int(input())

n_bridges = inp


my_parent = {}
is_parent = {}
child_count = {}


for i in range(n_bridges):
    inp = input().split()
    a = inp[0]
    b = inp[1]
    if not a in is_parent:
        is_parent[a] = True
        my_parent[a] = a #a bit unsure about disone
        child_count[a] = 1 #counts itself as its own child

    elif not is_parent[a]:
        while is_parent[a] == False:
            parent = my_parent[a]
            if not is_parent[parent]:
                my_parent[a] = my_parent[parent]
            a = my_parent[a]
    
    if not b in is_parent:
        is_parent[b] = True
        my_parent[b] = b
        child_count[b] = 1
    
    elif not is_parent[b]:
        
        while not is_parent[b]:
            
            parent = my_parent[b]
            if not is_parent[parent]:
                my_parent[b] = my_parent[parent]
            else:
                b = my_parent[b]
    
    
    if not a == b: #doesnt matter if the nodes have the same parent, they could reach eachother either way
        if child_count[a] > child_count[b]: #appending the parents
            child_count[a] += child_count[b]
            is_parent[b] = False
            my_parent[b] = a
            print(child_count[a])

        else:
            child_count[b] += child_count[a]
            is_parent[a] = False
            my_parent[a] = b
            print(child_count[b])
    
    else:
        print(child_count[a])




