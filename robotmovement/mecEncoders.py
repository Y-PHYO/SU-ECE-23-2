from roboclaw import Roboclaw
from time import sleep

roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

# Reset encoders and read and print value to test operation
roboclaw.ResetEncoders(0x80)
motor_1_count = roboclaw.ReadEncM1(0x80)
print ("After resetting:")
print (motor_1_count)

roboclaw.ResetEncoders(0x80)
motor_2_count = roboclaw.ReadEncM2(0x80)
print ("After resetting:")
print (motor_2_count)

roboclaw.ResetEncoders(0x81)
motor_1_count = roboclaw.ReadEncM1(0x81)
print ("After resetting:")
print (motor_1_count)

roboclaw.ResetEncoders(0x81)
motor_2_count = roboclaw.ReadEncM2(0x81)
print ("After resetting:")
print (motor_2_count)

sleep(2)

# Position motor, these values may have to be changed to suit the motor/encoder combination in use

# forward 
# changed from 10000 to 500 3rd last
# 2nd 2000 to 500
roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,500,5000,1)

# backward
roboclaw.SetEncM2(0x80,5000)
roboclaw.SetEncM1(0x80,5000)
roboclaw.SetEncM2(0x81,5000)
roboclaw.SetEncM1(0x81,5000)

roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,-500,0,1)

# right
roboclaw.SetEncM2(0x80,5000)
roboclaw.SetEncM1(0x81,5000)

roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,500,5000,1)

# left
roboclaw.SetEncM2(0x81,5000)
roboclaw.SetEncM1(0x80,5000)

roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,-500,0,1)

# rotate right
roboclaw.SetEncM2(0x81,5000)
roboclaw.SetEncM2(0x80,5000)

roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,-500,0,1)

address = 0x80
address2 = 0x81
speed1 = 1000
speed2 = 1000
distance = 6000

sleep(2)
print()
print(roboclaw.ReadSpeedM1(address))
print(roboclaw.ReadSpeedM2(address))
print(roboclaw.ReadSpeedM1(address2))
print(roboclaw.ReadSpeedM2(address2))
print()
print(roboclaw.ReadEncM1(address)[1])
print(roboclaw.ReadEncM2(address)[1])
print(roboclaw.ReadEncM1(address2)[1])
print(roboclaw.ReadEncM2(address2)[1])
