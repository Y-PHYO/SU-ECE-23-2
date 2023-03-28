# Runs LiDAR Scanner

from pyrplidar import PyRPlidar
import time
import numpy as np

def simple_scan():

    lidar = PyRPlidar()
    lidar.connect(port="/dev/ttyUSB0", baudrate=256000, timeout=3)
    # Linux   : "/dev/ttyUSB0"
    # MacOS   : "/dev/cu.SLAB_USBtoUART"
    # Windows : "COM5"

                  
    lidar.set_motor_pwm(500)
    time.sleep(3)
    arr_dist = []
    arr_angle = []
    len_count = []
    
    scan_generator = lidar.force_scan()
    for count,scan in enumerate(scan_generator()):
        #print(count, scan.distance)
        arr_dist.append(scan.distance)
        arr_angle.append(scan.angle)
        len_count.append(count)
        if count == 1600: break
    print(arr_dist)
    print(arr_angle)
    np.savetxt("data10.txt",(len_count,arr_dist,arr_angle),fmt="%d")
    
    lidar.stop()
    lidar.set_motor_pwm(0)

    
    lidar.disconnect()


if __name__ == "__main__":
    simple_scan()


