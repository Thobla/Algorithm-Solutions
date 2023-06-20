while True:
    inp = input()
    if inp == '.':
        break

    lps = [0] * len(inp) #longest prefix suffix (propper prefix that is also a suffix)
    pre_idx = 0
    idx = 1
    while idx < len(inp):
        if inp[pre_idx] == inp[idx]: #same character
            pre_idx += 1
            lps[idx] = pre_idx
            idx += 1
        else:
            if not (pre_idx == 0):
                pre_idx = lps[pre_idx - 1] #set it to previous
            else:
                lps[idx] = 0
                idx += 1
    
    
    #print(lps)
    highest_recurrence = max(lps)
    recurrence = len(inp) - highest_recurrence

    if highest_recurrence == 0:
        print(1)
    elif highest_recurrence != lps[-1]:
        print(1)
    elif (len(inp) % recurrence) == 0:
        print(int(len(inp) / recurrence))
    else:
        print(1)
        
    
        

