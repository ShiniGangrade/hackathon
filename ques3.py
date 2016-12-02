import math

# check value of number of people is even


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

number_of_people = int(raw_input("Enter number of people : "))
point = []
x_list = []
y_list = []


aaaa = []


for i in range(number_of_people):
    point.append(False)
    x_coor = int(raw_input("Enter x coordinate : "))
    x_list.append(x_coor)
    y_coor = int(raw_input("Enter y coordinate : "))
    y_list.append(y_coor)
    aaaa.append([x_coor,y_coor])

dist = {}
dist_list = []

pid = zip(range(number_of_people),x_list,y_list)

for i in range(0,number_of_people):
    for j in range(i+1,number_of_people):
        dist.update({(pid[i][0],pid[j][0]) : calculateDistance(pid[i][1],pid[i][2],pid[j][1],pid[j][2])})

for key, value in sorted(dist.iteritems(), key=lambda (k, v): (v, k)):
    dist_list.append([key,value])

cnt_flag = len(dist_list)

sum_dist = 0

while (cnt_flag > 0):
    d = dist_list.pop(0)
    if (point[d[0][0]] == False) and (point[d[0][1]] == False):
        print
        point1_id = pid[d[0][0]][0]
        point2_id = pid[d[0][1]][0]
        print "Removing points with id : ", point1_id , " and " , point2_id, " with distance ", d[1]
        point[point1_id] = True
        point[point2_id] = True
        sum_dist += d[1]
    cnt_flag -= 1
print "Total distance = ", sum_dist
