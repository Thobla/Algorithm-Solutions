from collections import deque
inp = input().split()

n_students = int(inp[0])
m_answers = int(inp[1])

possible_combs = 2 ** m_answers


def get_bin(number): #gets the binary of number as string, with string_length m_answers
    bin_str = bin(number)
    bin_str = bin_str[2:]
    return bin_str.rjust(m_answers, "0") # fills it with 0-s to the left


student_answers = deque([])
for i in range(n_students):
    answer = input()
    bin_answer = ""
    for elem in answer:
        if elem == "T":
            bin_answer += "1"
        elif elem == "F":
            bin_answer += "0"
    student_answers.append(bin_answer)

lowest_score = 0
for i in range(possible_combs): #goes through all possible combinations of answers, very cool, very O
    data = get_bin(i) #get the value as binary string
    curr_score = m_answers


    for k in range(len(student_answers)):
        student_score = m_answers
        student = student_answers[k]
        j = 0

        for elem in data: # will i increase with 1 for each itteration?
            if elem != student[j]: #is indexing of string effective?????? or O(n) mayhaps?
                student_score -= 1 
            j += 1

        if student_score < curr_score: #gets the lowest score
            curr_score = student_score

        
    if curr_score > lowest_score:
        lowest_score = curr_score    

print(lowest_score)







