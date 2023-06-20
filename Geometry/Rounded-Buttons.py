inp = int(input())



    


    

    


def is_inside(x, y):
    for elem in rects:
        if inside_rect(x, y, elem[0], elem[1], elem[2], elem[3]):
            return True
    
    for elem in sircles:
        if inside_sircle(x, y, elem[0], elem[1], elem[2]):
            return True
    
    return False



def inside_rect(click_x, click_y, start_x, start_y, end_x, end_y):

        if click_x >= start_x and click_x <= end_x:
            if click_y >= start_y and click_y <= end_y:
                return True

        return False
    
def inside_sircle(click_x, click_y, pos_x, pos_y, radius):
    
    dist_square = abs(click_x - pos_x) ** 2 + abs(click_y - pos_y) ** 2 # dont really need to square it, takes too much time
    
    if radius ** 2 >= dist_square:
        return True
    return False

for i in range(inp):
    inp = input().split()

    x_pos = float(inp[0])
    y_pos = float(inp[1])

    width = float(inp[2])
    height = float(inp[3])
    radius = float(inp[4])
    

    clicks = []

    for i in range(6, len(inp), 2): 
        clicks.append([float(inp[i]), float(inp[i+1])])


    rects = []
    sircles = []


    
    rects.append([x_pos + radius, y_pos, x_pos + width - radius, y_pos + height])
    rects.append([x_pos, y_pos + radius, x_pos + width, y_pos + height - radius])

    sircles.append([x_pos + radius, y_pos + radius, radius])
    sircles.append([x_pos + width - radius, y_pos + radius, radius])
    sircles.append([x_pos + radius, y_pos + height - radius, radius])
    sircles.append([x_pos + width - radius, y_pos + height - radius, radius])

    for elem in clicks:
        if is_inside(elem[0], elem[1]):
            print("inside")
        else:
            print("outside")
    print("")
    




