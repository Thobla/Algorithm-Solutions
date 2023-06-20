employee_count = int(input())

ceo = None
employee_children = {}
employee_speed = {}
employee_index = {}

for i in range(employee_count):
    
    inp = input().split()
    
    employee_speed[inp[0]] = float(inp[1])


    if not inp[2] in employee_children:
        employee_children[inp[2]] = None
    if not inp[0] in employee_children:
        employee_children[inp[0]] = None

    
    if inp[2] == "CEO":
        ceo = inp[0]

    else:

        if employee_children[inp[2]] == None:
            employee_children[inp[2]] = [inp[0]]
        else:
            employee_children[inp[2]].append(inp[0])


employee_list = []
for i in range(employee_count):
    employee_list.append([None, None, []]) #[parent_index, speed, [children]]

employee_list[0][1] = employee_speed[ceo]
employee_list[0][2] = employee_children[ceo]
employee_index[ceo] = 0

index = 0
def assign_index(parent_index, parent):
    global index
    if not employee_children[parent] == None:
        for elem in employee_children[parent]:
            index += 1
            employee_index[elem] = index
            employee_list[index][0] = parent_index
            employee_list[index][1] = employee_speed[elem]
            assign_index(index, elem)

assign_index(0, ceo)
index = 0
def assign_children(parent):
    global index
    if not employee_children[parent] == None:
        new_children_list = []
        for elem in employee_children[parent]:
            new_children_list.append(employee_index[elem])
            assign_children(elem)
        employee_list[employee_index[parent]][2] = new_children_list

assign_children(ceo)

dp_pick = []
dp_skip = []
for i in range(employee_count):
    dp_pick.append(None)
    dp_skip.append(None)

for i in range(employee_count-1, -1, -1):
    picked = [0, 0]
    skiped = [0, 0]
    if not employee_list[i][0] == None: #if not the ceo
        picked[0] += 1
        picked[1] += min(employee_list[i][1], employee_list[employee_list[i][0]][1])
        for elem in employee_list[i][2]:
            picked[0] += dp_skip[elem][0]
            picked[1] += dp_skip[elem][1]
    dp_pick[i] = picked


    if employee_list[i][2] == None:
        skiped = [0, 0]
    else:
        potential = [None, 0, 0, 0]
        for elem in employee_list[i][2]:
            if dp_pick[elem][0] - dp_skip[elem][0] == potential[1]:
                if dp_pick[elem][1] - dp_skip[elem][1] > potential[3]: #something iffy here
                    potential = [elem, dp_pick[elem][0] - dp_skip[elem][0], min(dp_pick[elem][1], dp_skip[elem][1]), dp_pick[elem][1] - dp_skip[elem][1]]
            elif dp_pick[elem][0] - dp_skip[elem][0] > potential[1]:
                potential = [elem, dp_pick[elem][0] - dp_skip[elem][0], min(dp_pick[elem][1], dp_skip[elem][1]), dp_pick[elem][1] - dp_skip[elem][1]]

        for elem in employee_list[i][2]:
            if potential[0] == None:
                skiped[0] += dp_skip[elem][0]
                skiped[1] += dp_skip[elem][1]
            elif not potential[0] == elem:
                skiped[0] += dp_skip[elem][0]
                skiped[1] += dp_skip[elem][1]
            else:
                skiped[0] += dp_pick[elem][0]
                skiped[1] += dp_pick[elem][1]
    dp_pick[i] = picked
    dp_skip[i] = skiped

    #print(i, skiped)
    #print(i, picked)
#print(employee_list)
print(dp_skip[0][0], round(dp_skip[0][1]/dp_skip[0][0], 3))