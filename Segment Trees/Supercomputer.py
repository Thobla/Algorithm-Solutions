

inp = input().split()

bits = int(inp[0])
queries = int(inp[1])


segment_tree = []
for i in range(2*bits): #starting at 1, memory is in the second half
    segment_tree.append(0)
if not bits % 2 == 0:
    segment_tree.append(0) #We still have equal amount of parents, but not leaf nodes


def flip(i):
    fliped_to_one = False

    if segment_tree[i - 1 + bits] == 0:
        segment_tree[i - 1 + bits] = 1
        fliped_to_one = True
    else:
        segment_tree[i - 1 + bits] = 0
    

    update((i - 1 + bits)//2, fliped_to_one) 



def update(i, flip_to_one):
    
    if flip_to_one:
        segment_tree[i] += 1
    else:
        segment_tree[i] -= 1
    if i == 1:
        return
    update(i//2, flip_to_one)


def count(start, end):
    res = 0

    if start == end:
        return segment_tree[start]
    res += segment_tree[start]
    res += segment_tree[end]
    while True:
        parent_start = start // 2
        parent_end = end // 2
        if parent_start == parent_end:
            return res
        if start % 2 == 0:
            res += segment_tree[parent_start * 2 + 1]
        if end % 2 == 1:
            res += segment_tree[parent_end * 2]
        start = parent_start
        end = parent_end



for i in range(queries):
    inp = input().split()
    if inp[0] == "F":
        flip(int(inp[1]))
    elif inp[0] == "C":
        print(count(int(inp[1]) - 1 + bits, int(inp[2]) - 1 + bits))

