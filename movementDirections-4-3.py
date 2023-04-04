# Runs Mecanum Wheels
import sys
from roboclaw import Roboclaw
from time import sleep
from threading import Thread
import math

#address1 = Roboclaw.SetEncM1(0x08,10000)
address = 0x80
address2 = 0x81
roboclaw = Roboclaw("/dev/ttyS0", 38400)
#roboclaw = Roboclaw("/dev/ttyAMA0", 38400)
roboclaw.Open()

# def funct1():
#     roboclaw.ForwardM1(address ,30)
#     roboclaw.ForwardM1(address2 ,30)
# def funct2():
#     roboclaw.ForwardM2(address ,30)
#     roboclaw.ForwardM2(address2 ,30)
    
def direction(x,y): # x and y values go from -1 to 1
    angle = math.atan2(y,x)
    return angle

def magnitude(a,b): # magnitudes are 0 to 1
    c = math.sqrt(a**2 + b**2)
    if (c > 1):
        c = 1
    return c

# correct speed is magnitude * speed

def power(x,y): # x is the angle, y is the magnitude
    FR = math.sin(x - (0.25 * math.pi)) # front right and back left wheels
    BL = math.sin(x - (0.25 * math.pi)) # front right and back left wheels
    FL = math.sin(x + (0.25 * math.pi)) # front left and back right wheels
    BR = math.sin(x + (0.25 * math.pi)) # front left and back right wheels
    FRspeed = (FR * y)
    BLspeed = (BL * y)
    FLspeed = (FL * y)
    BRspeed = (BR * y)
    if ((FRspeed > 1 or FRspeed < -1) or (BLspeed > 1 or BLspeed < -1) or (FLspeed > 1 or FLspeed < -1) or (BRspeed > 1 or BRspeed < -1)):
        allNum = [FRspeed, BLspeed, FLspeed, BRspeed]
        maxNum = max(allNum)
        minNum = min(allNum)
        if maxNum > abs(minNum):
            factor = abs(maxNum)
            FRspeed = FRspeed/factor
            BLspeed = BLspeed/factor
            FLspeed = FLspeed/factor
            BRspeed = BRspeed/factor
        elif maxNum < abs(minNum):
            factor = abs(minNum)
            FRspeed = FRspeed/factor
            BLspeed = BLspeed/factor
            FLspeed = FLspeed/factor
            BRspeed = BRspeed/factor
            
    return FLspeed, FRspeed, BLspeed, BRspeed
            
def move(magTest,pFL,pFR,pBL,pBR):
    pFL = pFL * 60
    pFR = pFR * 61
    pBL = pBL * 60
    pBR = pBR * 61
    pFL = int(pFL)
    pFR = int(pFR)
    pBL = int(pBL)
    pBR = int(pBR)
    print(pFL)
    print(pFR)
    print(pBL)
    print(pBR)
    sleep(0.001)
    if (pFL > 0):
        roboclaw.ForwardM1(address,pFL)
    elif (pFL < 0):
        roboclaw.BackwardM1(address,abs(pFL))
    sleep(0.001)
    if (pFR > 0):
        roboclaw.ForwardM2(address,pFR)
    elif (pFR < 0):
        roboclaw.BackwardM2(address,abs(pFR))
    sleep(0.001)
    if (pBL > 0):
        roboclaw.ForwardM1(address2,pBL)
    elif (pBL < 0):
        roboclaw.BackwardM1(address2,abs(pBL))
    sleep(0.001)
    if (pBR > 0):
        roboclaw.ForwardM2(address2,pBR)
    elif (pBR < 0):
        roboclaw.BackwardM2(address2,abs(pBR))
    sleep(6)
    
    roboclaw.ForwardM1(address,0)
    roboclaw.ForwardM2(address,0)
    roboclaw.ForwardM1(address2,0)
    roboclaw.ForwardM2(address2,0)
    
def test(xD,yD):
    xDir = xD
    yDir = yD
    angleTest = direction(xDir,yDir)
    print("Angle: " + str(math.degrees(angleTest)))
    magTest = magnitude(xDir,yDir)
    print("Magnitude: " + str(magTest))
    powerTest = power(angleTest,magTest)
    print("Power: " + str(powerTest))
    pFL = float(powerTest[0])
    pFR = float(powerTest[1])
    pBL = float(powerTest[2])
    pBR = float(powerTest[3])
    print(pFL)
    print(pFR)
    print(pBL)
    print(pBR)
    move(magTest,pFL,pFR,pBL,pBR)


def moveRight():
    xDir = 1
    yDir = 0
    test(xDir, yDir)


def moveLeft():
    xDir = -1
    yDir = 0
    test(xDir, yDir)


def moveForward():
    xDir = 0
    yDir = 1
    test(xDir, yDir)


def moveBack():
    xDir = 0
    yDir = -1
    test(xDir, yDir)

            
if __name__ == '__main__':
    moveForward()

#     Thread(target = funct1).start()
#     sleep(0.0001)
#     Thread(target = funct2).start()
#     sleep(1)
#     roboclaw.ForwardM1(address,0)
#     roboclaw.ForwardM1(address2,0)
#     roboclaw.ForwardM2(address,0)
#     roboclaw.ForwardM2(address2,0)

#     Right
#     xDir = 1
#     yDir = 0
#     test(xDir,yDir) # 90 degrees

#     xDir = 1
#     yDir = 1
#     test(xDir,yDir) # 45 degrees
#     sleep(5)
#     xDir = -1
#     yDir = -1
#     test(xDir,yDir) # -135 degrees or 225 degrees
#     sleep(5)
#     xDir = -1
#     yDir = 1
#     test(xDir,yDir) # 135 degrees
#     sleep(5)
#     xDir = 1
#     yDir = -1
#     test(xDir,yDir) # -45 degrees or 315 degrees
    
    
    
