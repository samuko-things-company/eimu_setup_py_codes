import numpy as np
import time
from termcolor import colored
from serial_comm_lib import SerialComm


portName = '/dev/ttyUSB0'
imu = SerialComm(portName)


for i in range(10):
  time.sleep(1.0)
  print(colored(f"{i+1} sec", 'yellow'))
  

no_of_samples = 1000

roll_arr = []
pitch_arr = []
yaw_arr = []


def main():
  for i in range(no_of_samples):
    r_rad, p_rad, y_rad = imu.get('/rpy')
    roll_arr.append(r_rad)
    pitch_arr.append(p_rad)
    yaw_arr.append(y_rad)

    percent = (i*100)/no_of_samples
    print(colored(f"reading_sensor_data...  {percent} percent complete", 'grey'))

    time.sleep(0.02)
  
  roll_variance = np.var(roll_arr)
  pitch_variance = np.var(pitch_arr)
  yaw_variance = np.var(yaw_arr)

  rpy_variance = [ roll_variance, pitch_variance, yaw_variance ]
  print(colored("\n---------------------------------------------------------------", 'magenta'))
  print(colored("computed rpy variances:", 'cyan'))
  print(rpy_variance)

  imu.send('/rpy-var', roll_variance, pitch_variance, yaw_variance)
  roll_variance, pitch_variance, yaw_variance = imu.get('/rpy-var')

  rpy_variance = [ roll_variance, pitch_variance, yaw_variance ]
  print(colored("stored rpy variances", 'green'))
  print(rpy_variance)
  print(colored("---------------------------------------------------------------", 'magenta'))


if __name__ == "__main__":
  main()