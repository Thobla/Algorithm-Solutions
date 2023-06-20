cases = int(input())

# c complexity
for case in range(cases):
    result = 0
    inp = input().split()
    divisor = int(inp[0])
    sequence_length = int(inp[1])

    sequence = input().split()
    prefix_sum_mod = []
    counter = 0
    for elem in sequence: #n
        if counter == 0:
            prefix_sum_mod.append(int(elem) % divisor)
        else:
            prefix_sum_mod.append((prefix_sum_mod[counter - 1] + int(elem)) % divisor)
        
        counter += 1


    count_list = []
    for i in range(divisor): # d complexity
        count_list.append(0)

    for elem in prefix_sum_mod:
        count_list[elem] += 1
    
    counter = 0
    for elem in count_list:
        if counter == 0:
            if elem > 0:
                result += int((elem * (elem + 1)) / 2)
            counter = 1
        elif counter == 1:
            if elem > 1:
                result += int((elem * (elem - 1)) / 2)
    
    print(result)