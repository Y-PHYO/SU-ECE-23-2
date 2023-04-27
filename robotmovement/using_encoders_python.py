from roboclaw import Roboclaw
from time import sleep

roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()


# Read encoder
#motor_1_count = roboclaw.ReadEncM1(0x80)
#print ("Original:")
#print (motor_1_count)

#sleep(2)

# Set encoder and then read and print to test operation
#roboclaw.SetEncM1(0x80, 10000)
#motor_1_count = roboclaw.ReadEncM1(0x80)
#print ("After setting count:")
#print (motor_1_count)

sleep(2)

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
# forward changed from 10000 to 500 3rd last
# 2nd 2000 to 500
#roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,500,5000,0)
#roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,500,5000,0)
#roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,500,5000,0)
#roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,500,5000,1)

# backward
#roboclaw.SetEncM2(0x80,5000)
#roboclaw.SetEncM1(0x80,5000)
#roboclaw.SetEncM2(0x81,5000)
#roboclaw.SetEncM1(0x81,5000)

#roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,-500,0,0)
#roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,-500,0,0)
#roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,-500,0,0)
#roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,-500,0,1)

# right
roboclaw.SetEncM2(0x80,5000)
roboclaw.SetEncM1(0x81,5000)

roboclaw.SpeedAccelDeccelPositionM1(0x80,500,500,500,5000,0)
roboclaw.SpeedAccelDeccelPositionM2(0x80,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM1(0x81,500,500,-500,0,0)
roboclaw.SpeedAccelDeccelPositionM2(0x81,500,500,500,5000,1)

#roboclaw.SpeedM1M2(0x80, -1000, -1000)
#roboclaw.SpeedM1M2(0x81, -1000, -1000)
#roboclaw.SpeedAccelDeccelPositionM1M2(0x80,10000,1000,10000,5000,10000,1000,10000,5000,1)
#roboclaw.SpeedAccelDeccelPositionM1M2(0x81,10000,1000,10000,5000,10000,1000,10000,5000,1)
#sleep(1)
#roboclaw.ResetEncoders(0x80)
#roboclaw.ResetEncoders(0x81)

#roboclaw.SpeedDistanceM1(0x80,500,2000,1)
#roboclaw.SpeedDistanceM2(0x80,500,2000,1)
#roboclaw.SpeedDistanceM1(0x81,500,2000,1)
#roboclaw.SpeedDistanceM2(0x81,500,2000,1)
#print(roboclaw.ReadMainBatteryVoltage(0x80))
#print(roboclaw.ReadMainBatteryVoltage(0x81))

#sleep(10)
#roboclaw.SpeedAccelDeccelPositionM1M2(0x80,10000,1000,10000,0,10000,1000,10000,0,1)
#roboclaw.SpeedAccelDeccelPositionM1M2(0x81,10000,1000,10000,0,10000,1000,10000,0,1)
#sleep(4)
#roboclaw.SpeedM1M2(0x80, 0, 0)
#roboclaw.SpeedM1M2(0x81, 0, 0)
#sleep(1)
#roboclaw.SpeedM1M2(0x80, 1000, 1000)
#roboclaw.SpeedM1M2(0x81, 1000, 1000)
#sleep(4)
#roboclaw.SpeedM1M2(0x80, 0, 0)
#roboclaw.SpeedM1M2(0x81, 0, 0)

address = 0x80
address2 = 0x81
#speed = 1000
speed1 = 1000
speed2 = 1000
distance = 6000
#roboclaw.SetM1VelocityPID(address,1,2,0,44000)
#roboclaw.SetM2VelocityPID(address,1,1,1,44000)
#roboclaw.SetM1VelocityPID(address2,1,2,0,44000)
#roboclaw.SetM2VelocityPID(address2,1,1,1,44000)
#sleep(2)
#roboclaw.ForwardM1(address,24)
#roboclaw.SpeedM1(address,500)
#roboclaw.SpeedM2(address,505)
#roboclaw.SpeedM1(address2,500)
#roboclaw.SpeedM2(address2,505)
#sleep(0.001)
#roboclaw.ForwardM2(address,25)
#sleep(0.001)
#roboclaw.ForwardM1(address2,24)
#sleep(0.001)
#roboclaw.ForwardM2(address2,25)
#sleep(0.001)
#roboclaw.SpeedDistanceM1M2(address,speed1,distance,speed2,distance,1)
#while (roboclaw.ReadEncM1(address)[1] + roboclaw.ReadEncM2(address)[1] + roboclaw.ReadEncM1(address2)[1] + roboclaw.ReadEncM2(address2)[1]) / 4 < distance:
#    pass
sleep(2)
print()
print(roboclaw.ReadSpeedM1(address))
print(roboclaw.ReadSpeedM2(address))
print(roboclaw.ReadSpeedM1(address2))
print(roboclaw.ReadSpeedM2(address2))
#sleep(1)
#roboclaw.ForwardM1(address,127)
#roboclaw.ForwardM2(address,127)
#roboclaw.ForwardM1(address2,127)
#roboclaw.ForwardM2(address2,127)
print()
#sleep(1)
print(roboclaw.ReadEncM1(address)[1])
print(roboclaw.ReadEncM2(address)[1])
print(roboclaw.ReadEncM1(address2)[1])
print(roboclaw.ReadEncM2(address2)[1])
#sleep(5)
#print(roboclaw.ReadSpeedM1(address))
#print(roboclaw.ReadSpeedM2(address))
#print(roboclaw.ReadSpeedM1(address2))
#print(roboclaw.ReadSpeedM2(address2))
#sleep(1)
#roboclaw.ForwardM1(address,0)
#sleep(0.001)
#roboclaw.ForwardM2(address,0)
#sleep(0.001)
#roboclaw.ForwardM1(address2,0)
#sleep(0.001)
#roboclaw.ForwardM2(address2,0)
