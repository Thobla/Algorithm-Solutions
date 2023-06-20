goals = []

while True:
    try:
        read = input()
        goals.append(read)
    except:
        break




#player defines wether stan (0) or ollie (1) is the current player
def opt(n, player):

    memo0 = {} #
    memo1 = {}
    #base case
    if n in memo1 and player == 1:
        return memo1[n]
    elif n in memo0 and player == 0:
        return memo0[n]

    if n <= 9:
        return player

    if(player == 1):
        winner = max(opt(n/2, next(player)), opt(n/9, next(player)))
        memo1[n] = winner
    elif(player == 0):
        winner = min(opt(n/2, next(player)), opt(n/9, next(player)))
        memo0[n] = winner

    
    return winner

def next(i):
    if i == 0:
        return 1
    elif i == 1:
        return 0

for goal in goals:
    result = opt(int(goal), 1)
    if result == 1:
        print("Stan wins.")
    elif result == 0:
        print("Ollie wins.")