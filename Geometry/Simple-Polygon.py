#2
#4 0 0 2 0 0 1 1 0
#5 0 0 10 0 10 5 5 -1 0 5
from collections import deque

for _ in range(int(input())):
    inp = list(map(int, input().split()))
    points = deque((inp[i], inp[i + 1]) for i in range(1, inp[0] * 2, 2))
    point_index = {}
    
    for i in range(len(points)):
        point_index[points[i]] = str(i)

    points = deque(sorted(points))
    
    itt_points = deque([])
    points_left = deque([])


    while len(points) > 0:
        pos = points.popleft()
        while len(itt_points) > 1:
            v_1, v_2 = (itt_points[-2][0] - itt_points[-1][0], itt_points[-2][1] - itt_points[-1][1]), (itt_points[-1][0] - pos[0], itt_points[-1][1] - pos[1])
            cross = v_1[0] * v_2[1] - v_2[0] * v_1[1]
            if cross < 0: #cross >=? No because we want to include them if on same line
                points_left.appendleft(itt_points.pop())

            else:
                break
        itt_points.append(pos)
    
    points_left = deque((sorted(points_left)))

    while len(points_left) > 0:
        itt_points.append(points_left.pop())
    
    res = " ".join(point_index[elem] for elem in itt_points)

    print(res)
    
