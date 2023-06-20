
while True:
    nodes = int(input())

    if nodes == 0:
        break

    points = [] # [(x, y)]
    for i in range(nodes):
        inp = input().split()
        x = int(inp[0])
        y = int(inp[1])
        points.append([x, y])


    area_pos = 0
    area_neg = 0

    for i in range(len(points)):
        
        area_pos += points[i-1][0] * points[i][1]
        area_neg += points[i-1][1] * points[i][0]

    is_clockwise = True

    if area_pos - area_neg > 0:
        is_clockwise = False

    if is_clockwise:
        print("CW " + str(abs(area_pos - area_neg) / 2.0))
    
    else:
        print("CCW " + str(abs(area_pos - area_neg) / 2.0))



