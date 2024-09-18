import time
from termcolor import colored
from serial_comm_lib import SerialComm


portName = '/dev/ttyUSB0'
imu = SerialComm(portName)

frameList = ["NWU", "ENU", "NED"]


for i in range(10):
  time.sleep(1.0)
  print(colored(f"{i+1} sec", 'light_yellow'))


def main():
  # frameId = 1 ## 0 - NWU,  1 - ENU,  2 - NED
  # isSuccessful = imu.send("/frame-id", frameId)
  isSuccessful = True
  if isSuccessful:
    storedFrameId = int(imu.get("/frame-id")) ## 0 - NWU,  1 - ENU,  2 - NED
    print(colored(f"\nSUCCESS: You are using the {frameList[storedFrameId]} frame", 'green'))
  else:
    print(colored("\nERROR: reference frame not successfully set\n", 'red'))


if __name__ == "__main__":
  main()
  