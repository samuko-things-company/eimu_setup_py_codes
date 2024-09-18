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

roll_rate_arr = []
pitch_rate_arr = []
yaw_rate_arr = []



def main():
  for i in range(no_of_samples):
    r_rate, p_rate, y_rate = imu.get('/gyro-cal')
    roll_rate_arr.append(r_rate)
    pitch_rate_arr.append(p_rate)
    yaw_rate_arr.append(y_rate)

    percent = (i*100)/no_of_samples
    print(colored(f"reading_sensor_data...  {percent} percent complete", 'grey'))

    time.sleep(0.02)


  roll_rate_variance = np.var(roll_rate_arr)
  pitch_rate_variance = np.var(pitch_rate_arr)
  yaw_rate_variance = np.var(yaw_rate_arr)


  gyro_variance = [ roll_rate_variance, pitch_rate_variance, yaw_rate_variance]
  print(colored("\n---------------------------------------------------------------", 'magenta'))
  print(colored("computed gyro variances:", 'cyan'))
  print(gyro_variance)

  imu.send('/gyro-var', roll_rate_variance, pitch_rate_variance, yaw_rate_variance)
  roll_rate_variance, pitch_rate_variance, yaw_rate_variance = imu.get('/gyro-var')

  gyro_variance = [ roll_rate_variance, pitch_rate_variance, yaw_rate_variance]
  print(colored("stored gyro variances", 'green'))
  print(gyro_variance)
  print(colored("---------------------------------------------------------------", 'magenta'))


if __name__ == "__main__":
  main()