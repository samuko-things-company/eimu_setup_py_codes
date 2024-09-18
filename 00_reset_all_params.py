import time
from termcolor import colored
from serial_comm_lib import SerialComm


portName = '/dev/ttyUSB0'
imu = SerialComm(portName)


for i in range(10):
  time.sleep(1.0)
  print(colored(f"{i+1} sec", 'light_yellow'))


def main():
  isSuccessful = imu.send("/reset")
  if isSuccessful:
    print(colored("\nSUCCESS: parameters reset successful", 'green'))
    print(colored("restart the imu cct to see effect.\n", 'cyan'))
  else:
    print(colored("\nERROR: parameters reset not successful\n", 'red'))


if __name__ == "__main__":
  main()
  