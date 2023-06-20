from collections import deque

inp = input().split()

n_islands = int(inp[0])
n_bridges = int(inp[1])




neighbours = [[] for i in range(n_islands + 1)]


for i in range(n_bridges):
    inp = input().split()
    isl_1 = int(inp[0])
    isl_2 = int(inp[1])


    neighbours[isl_1].append(isl_2)
    neighbours[isl_2].append(isl_1)


island_army = [0 for i in range(n_islands + 1)]
for i in range(1, n_islands + 1):
    inp = int(input())

    island_army[i] = inp




conquered = [False for i in range(n_islands + 1)]
conquered[1] = True

next_island = deque()
for elem in neighbours[1]:
    next_island.append(elem)


def conquer(queue):
    next_queue = deque()
    new_queue = False
    for i in range(len(queue)):
        island = queue.popleft()
        if not conquered[island]:

            if island_army[1] > island_army[island]:
                new_queue = True #We added atleast 1 island to the queue
                island_army[island]
                island_army[1] += island_army[island]
                island_army[island] = 0

                conquered[island] = True

                for elem in neighbours[island]:
                    if not conquered[elem]:
                        next_queue.appendleft(elem)

            else:
                next_queue.append(island)
    if new_queue:
        conquer(next_queue)

conquer(next_island)

print(island_army[1])
