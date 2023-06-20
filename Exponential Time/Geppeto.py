inp = input().split()

n_ingredients = int(inp[0])
m_illegal = int(inp[1])


n_combinations = 2 ** n_ingredients

def num_to_bin(value):
    bin_str = bin(value)[2:]
    return bin_str.rjust(n_ingredients, "0")


adj_list = [] #adj list for illegal contents >:(
for elem in range(n_ingredients + 1):
    adj_list.append([])

for i in range(m_illegal):
    inp = input().split()
    index = int(inp[0])
    illegal = int(inp[1])

    adj_list[index].append(illegal)

menu_size = 0
for i in range(n_combinations):
    recepie = num_to_bin(i)
    is_valid = True #any recepie is valid until proven guilty :)

    for j in range(1, n_ingredients + 1):
        if not is_valid:
            break
        if not adj_list[j] == None:
            if recepie[j - 1] == "1":
                
                for elem in adj_list[j]:
                    
                    if recepie[elem - 1] == "1":
                        is_valid = False
                    if not is_valid:
                        break
    if is_valid:
        menu_size += 1


print(menu_size)


