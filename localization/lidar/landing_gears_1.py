import numpy as np
import math
import cmath
import pandas as pd
import matplotlib.pyplot as plt
#from localizationFunctions import *
#from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import groupby

def pol2carteisan_x(rho,theta):
    x = rho * math.cos(theta)
    return x

def pol2carteisan_y(rho,theta):
    y = rho * math.sin(theta)
    return y

if __name__=="__main__":
    #landing gears
    radius = 130
    x1,x2,x3,y1,y2,y3 = 0,0,0,0,0,0
    angle_d ,dist,dist1,num,count,angle,x=[],[],[],[],[],[],[]
    # reading file
    filedata = pd.read_excel('data10.xlsx')
    #filedata = pd.read_excel('data1a.xlsx')
    df = pd.DataFrame(filedata)
    count_arr = df.iloc[:,[0]].to_numpy()
    dist_arr = df.iloc[:,[1]].to_numpy()
    angle_arr = df.iloc[:,[2]].to_numpy()

    dist = dist_arr.flat
    count = count_arr.flat
    angle = angle_arr.flat

    for i in range(len(dist)):
        # Eliminate the long distance
        if (dist[i] > 600) and (dist[i] < 1500):
            dist1.append(dist[i])
            angle_d.append(angle[i])
            num.append(count[i])

    #Angles are close between each landing gears
    dist_close, angle_close, R, theta, num_1,theta1 ,theta2,theta3= [], [], [], [], [],[],[],[]
    for i in range(0, len(num) - 1):
        if (math.fabs(angle_d[i] - angle_d[i + 1]) < 1): #1
            R.append(dist1[i])
            theta.append(angle_d[i])
            num_1.append(num[i])
    #sort R
    x = sorted(R)
    #Group if the distances between each points are 200mm close
    sub_lists = [list(group) for k, group in groupby(x, lambda i: i // 200)] #200

    print(sub_lists)
    landing1 = min(sub_lists[0])
    landing2 = min(sub_lists[1])
    landing3 = min(sub_lists[2])

    #find theta base on landing gear 1,2 and 3
    for i in range(len(R)):
        if landing1 == R[i]:
            theta1.append(theta[i])
        elif landing2 == R[i]:
            theta2.append(theta[i])
        elif landing3 == R[i]:
            theta3.append(theta[i])

    print(landing1," ",theta1)
    print(landing2," ",theta2)
    print(landing3," ",theta3)
    #Landing gear from the center
    #Landing = [landing1+130,landing2+130,landing3+130]
    Landing = [landing1 , landing2 , landing3 ]
    #Convert Polar to Cartesian coordinates
    x1 = pol2carteisan_x(Landing[0],theta1[0])
    x2 = pol2carteisan_x(Landing[1],theta2[0])
    x3 = pol2carteisan_x(Landing[2],theta3[0])
    y1 = pol2carteisan_y(Landing[0],theta1[0])
    y2 = pol2carteisan_y(Landing[1],theta2[0])
    y3 = pol2carteisan_y(Landing[2],theta3[0])

    print("Landing Gear 1: ", Landing[0], " Theta 1: ", theta1[0])
    print("Landing Gear 2: ", Landing[1], " Theta 2: ", theta2[0])
    print("Landing Gear 3: ", Landing[2], " Theta 3: ", theta3[0])
    print("X1: ", x1, " Y1: ",y1)
    print("X2: ", x2, " Y2: ", y2)
    print("X3: ", x3, " Y3: ", y3)






