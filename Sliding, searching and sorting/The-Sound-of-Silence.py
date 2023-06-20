#7 2 0              2   |   7 - n number of samples,  2 - m required length of silence, 0 - c maximal noise level allowed within silence
#0 1 1 2 3 2 2      6   |   print out start index of silence + 1
from collections import deque
inp = input().split()

n_samples = int(inp[0])
m_silence_length = int(inp[1])
c_maximal_noise = int(inp[2])

inp = input().split()


main_queue = deque([]) # our main queue of size m after fully innitialized
low_queue = deque([]) # queue containing the min values (size 1 <= size <= m)
high_queue = deque([]) # queue containing the max values (size 1 <= size <= m)






#is_high = true, value = 1, high_queue = [0]
def queue_action(queue, value, is_high): #PS! SHOULD HAPPEN AFTER REMOVING queue[0], also is_high = true when high_queue, is_high == false when low_queue
    
        
    if not queue:
        queue.append(value)
  

    else:
        while(1):#repeats until queue[-1] >= value
            
            if (not queue):
                queue.append(value)
                break

            if (queue[-1] >= value and is_high) or (queue[-1] <= value and not is_high):
                queue.append(value)
                break
            
            elif (queue[-1] < value and is_high) or (queue[-1] > value and not is_high):
                queue.pop() #removes the last element
    #else:
    #   ValueError("should not be able to get here") # JUST in case, so easier to debug



if m_silence_length > n_samples:
    print("NONE")



# TODO figure out complexity of deque[-1], imagine it would be O(1) unless it goes all the way from front to back
else:
    result = []
    for i in range(m_silence_length):
        value = int(inp[i])
        main_queue.append(value)
        queue_action(high_queue, value, True)#updating the queues
        queue_action(low_queue, value, False)
        

    
    for i in range(m_silence_length, n_samples + 1):
        if high_queue[0] - low_queue[0]  <= c_maximal_noise:
            result.append(i - m_silence_length + 1) #adding the start index+1 of the window to the result list


        first_value = main_queue[0]

        if high_queue[0] == first_value:
            high_queue.popleft() #removes the left most element as this is not in the window anymore
        if low_queue[0] == first_value:
            low_queue.popleft()
        if i < n_samples: 
            value = int(inp[i])
            main_queue.append(value)
            main_queue.popleft() #removes the left most element as this is not in the window anymore

            queue_action(high_queue, value, True)
            queue_action(low_queue, value, False)
            
        
    if len(result) == 0:
        print("NONE")    
    else:
        for elem in result:
            print(elem)

        