points = sorted([tuple(map(float, input().split())) for _ in range(int(input()))]) #Eg er et Geni!!!!!
print(max([abs(points[i][1] - points[i-1][1]) / abs(points[i][0] - points[i-1][0]) for i, points in range(1, len(points))]))