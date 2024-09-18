import time
from termcolor import colored
from serial_comm_lib import SerialComm


portName = '/dev/ttyUSB0'
imu = SerialComm(portName)

for i in range(10):
  time.sleep(1.0)
  print(colored(f"{i+1} sec", 'light_yellow'))
  

def set_i2c_address(val):
  # isSuccessful = imu.send("/i2c", val)
  isSuccessful = True
  if isSuccessful:
    i2c_address = int(imu.get("/i2c"))
    print(colored(f"\nSUCCESS: 12c address successfully set to: {i2c_address}", 'green'))
    print(colored("restart the imu cct to see effect.\n", 'cyan'))
  else:
    print(colored("\nERROR: 12c address not successfully set\n", 'red'))


if __name__ == "__main__":
  set_i2c_address(18) # change this. default 104 (i.e 0x68)