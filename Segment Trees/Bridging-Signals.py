seq_len = int(input())

seq = []

for elem in range(seq_len):
    seq.append(int(input()))


def binSearch(arr, l, r, val): # Creating a binary search to find the first value larger than it (returns the index of leftmost value it UNDERtakes)
    curr_r = r #the rightmost index
    curr_l = l # the leftmost index

    while curr_r  > curr_l + 1: # runs while the gap between curr_l and curr_r is 1 (next itteration could make curr_r = curr_l)
        mid_index = curr_l + (curr_r - curr_l) // 2
        if arr[mid_index] < val:
            curr_l = mid_index # val still have not found a value larger than it, so it must be to its right
        else:
            curr_r = mid_index # Val was smaller than the middle-value, but it may still be larger than some values to the left
        
    return curr_r 



currSeq = [0] * seq_len #array containing the current longest sequence
currSeq[0] = seq[0] #we add the innitial element
len = 1

for i in range(1, seq_len): #all indexes in sequence, except for 0, since already added
    if currSeq[0] > seq[i]: # We have new base for a sequence
        currSeq[0] = seq[i]
    
    elif currSeq[len-1] < seq[i]: #larger than last element in current sequence
        currSeq[len] = seq[i] #add value to sequence
        len += 1 #longest length increases

    else:
        index = binSearch(currSeq, 0, len, seq[i]) #finding where to insert the value
        currSeq[index] = seq[i] #changing the current sequence by adding it to one of the subsequences


print(len)

