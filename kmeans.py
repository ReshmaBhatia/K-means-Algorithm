import math
import random
import matplotlib.pyplot as plt

x_points = []
y_points = []
with open('C:\Users\RESHMA BHATIA\Desktop\Machine Learning\hw2\clusters.txt') as filestream:
    for line in filestream:
        x,y = line.split(",")
        y = y.rstrip('\n')
        x_points.append(x)
        y_points.append(y)

for x in x_points:
    x_points[x_points.index(x)] = float(x)

for y in y_points:
    y_points[y_points.index(y)] = float(y)

#print (x_points)
#print (y_points)

#Calculating Euclidean Distance
def euclidean_distance(x1,y1,CX1,CY1):
    a=x1-CX1
    #print (a)
    b=y1-CY1
    c=math.pow(a,2)
    d=math.pow(b,2)
    e=c+d
    f=math.sqrt(e)
    return f

#Calculating Mean
def mean(cluster_list):
    x_sum = 0
    y_sum = 0
    mean_coord = []
    for i in cluster_list:
       x_sum+=x_points[i]
       y_sum+=y_points[i]
    count=len(cluster_list)
    x_coord=x_sum/count
    mean_coord.append(x_coord)
    y_coord=y_sum/count
    mean_coord.append(y_coord)
    return mean_coord

#Calling Euclidean Distance and mean function
def Kmean(A):
    C1_list = []
    C2_list = []
    C3_list = []
    final = []
    for i in range(0,len(x_points)):
        a=euclidean_distance(x_points[i],y_points[i],A[0][0],A[0][1])
        #print ('Ea=',a)
        b=euclidean_distance(x_points[i],y_points[i],A[1][0],A[1][1])
        c=euclidean_distance(x_points[i],y_points[i],A[2][0],A[2][1])
        minimum=min(a,b,c)
        if minimum==a:
            C1_list.append(i)
        elif minimum==b:
            C2_list.append(i)
        else:
            C3_list.append(i)

    meanC1=mean(C1_list)
    meanC2=mean(C2_list)
    meanC3=mean(C3_list)
    #print("meanC1=", meanC1,"meanC2=", meanC2,"meanC3=", meanC3)
    final.append(meanC1)
    final.append(meanC2)
    final.append(meanC3)
    return final



#def root(x_points, y_points):
C1 = []
C2 = []
C3 = []
centroids = []
#result = [[], [], []]
result_empty = [[], [], []]
#Selecting Random centroid points as initialization
randomCX1 = (random.choice(x_points))
randomCX2 = (random.choice(x_points))
if randomCX1==randomCX2:
    randomCX2 = (random.choice(x_points))
randomCX3 = (random.choice(x_points))
if randomCX1==randomCX3:
    randomCX3 = (random.choice(x_points))
if randomCX2==randomCX3:
    randomCX3== (random.choice(x_points))

p = x_points.index(randomCX1)
q = x_points.index(randomCX2)
r = x_points.index(randomCX3)
#print ('randomCX1=',randomCX1)

randomCY1 = y_points[p]
randomCY2 = y_points[q]
randomCY3 = y_points[r]

C1.append(randomCX1)
C1.append(randomCY1)
C2.append(randomCX2)
C2.append(randomCY2)
C3.append(randomCX3)
C3.append(randomCY3)

centroids.append(C1)
centroids.append(C2)
centroids.append(C3)

result=Kmean(centroids)

#Converging the centroid points
while result!=result_empty:
    result_empty=result
    result=Kmean(result)

print '3 Centroids of K-means Cluster are as follows:'
print(result_empty[0])
print(result_empty[1])
print(result_empty[2])

