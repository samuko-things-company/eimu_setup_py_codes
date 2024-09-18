from vpython import *
import numpy as np
import time as t
import math as m
from termcolor import colored
from serial_comm_lib import SerialComm


portName = '/dev/ttyUSB0'
imu = SerialComm(portName)

frameList = ["NWU", "ENU", "NED"]


for i in range(10):
  t.sleep(1.0)
  print(colored(f"{i+1} sec", 'yellow'))


toRad = 2*np.pi/360
toDeg = 1/toRad

# Set Gain of the filter.
# Higher values lead to faster convergence but more noise in reading.
# Lower values lead to slower convergence but less noise in reading
filterGain = 1.0 # default value = 1.0


def main():
  #----------------------------------------------------------------#
  # isSuccessful = imu.send("/gain", filterGain)
  gain = imu.get("/gain")
  print("Started with Filter Gain: ", gain)
  #----------------------------------------------------------------#


  ##----------------------------------------------------------------##
  scene.range=5
  scene.forward=vector(-1,-1,-1)
  scene.width=500
  scene.height=500

  xAxis = arrow(length=1.25, shaftwidth=.08, color=color.red,
                axis=vector(0,0,1), opacity=1.0) # (y,z,x)
  yAxis = arrow(length=1.25, shaftwidth=.08, color=color.green,
                axis=vector(1,0,0), opacity=1.0) # (y,z,x)
  zAxis = arrow(length=1.25, shaftwidth=.08, color=color.blue,
                axis=vector(0,1,0), opacity=1.0) # (y,z,x)
  
  myBox = box()
  myBox.length = 3.5
  myBox.width = 1.5
  myBox.height = 0.25
  myBox.opacity = 0.2

  storedFrameId = int(imu.get("/frame-id")) ## 0 - NWU,  1 - ENU,  2 - NED

  if frameList[storedFrameId] == "NWU":
    xArrow = arrow(length=3, shaftwidth=.1, color=color.red,
                  axis=vector(0,0,1), opacity=.3) # (y,z,x)
    yArrow = arrow(length=3, shaftwidth=.1, color=color.green,
                  axis=vector(1,0,0), opacity=.3) # (y,z,x)
    zArrow = arrow(length=3, shaftwidth=.1, color=color.blue,
                  axis=vector(0,1,0), opacity=.3) # (y,z,x)

  elif frameList[storedFrameId] == "ENU":
    xArrow = arrow(length=3, shaftwidth=.1, color=color.red,
                  axis=vector(0,0,1), opacity=.3) # (y,z,x)
    yArrow = arrow(length=3, shaftwidth=.1, color=color.green,
                  axis=vector(1,0,0), opacity=.3) # (y,z,x)
    zArrow = arrow(length=3, shaftwidth=.1, color=color.blue,
                  axis=vector(0,1,0), opacity=.3) # (y,z,x)
    
    myBox.length = 1.5
    myBox.width = 3.5
  
  elif frameList[storedFrameId] == "NED":
    xArrow = arrow(length=3, shaftwidth=.1, color=color.red,
                  axis=vector(0,0,1), opacity=.3) # (y,z,x)
    yArrow = arrow(length=3, shaftwidth=.1, color=color.green,
                  axis=vector(1,0,0), opacity=.3) # (y,z,x)
    zArrow = arrow(length=3, shaftwidth=.1, color=color.blue,
                  axis=vector(0,1,0), opacity=.3) # (y,z,x)
    

  myObj = compound([myBox])
  ##----------------------------------------------------------------##


  ##----------------------------------------------------------------##
  while True:
    roll, pitch, yaw = imu.get('/rpy')

    # print(m.degrees(roll), m.degrees(pitch), m.degrees(yaw))

    # if frameList[storedFrameId] == "NWU":
    #   ##### perform axis computations #####################
    #   up=np.array([0,0,1]) # (x,y,z)
    #   x_vect=np.array([m.cos(yaw)*m.cos(pitch), m.sin(yaw)*m.cos(pitch), -1.00*m.sin(pitch)]) # (x,y,z)
    #   y_vect = np.cross(up,x_vect) # (x,y,z)
    #   z_vect = np.cross(x_vect,y_vect) # (x,y,z)

    #   z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)
    #   # z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)+x_vect*np.dot(x_vect,z_vect)*(1-m.cos(roll))

    #   y_rot = np.cross(z_rot, x_vect)

    # elif frameList[storedFrameId] == "ENU":
    #   ##### perform axis computations #####################
    #   up=np.array([0,0,1]) # (x,y,z)
    #   x_vect=np.array([m.cos(yaw)*m.cos(pitch), m.sin(yaw)*m.cos(pitch), -1.00*m.sin(pitch)]) # (x,y,z)
    #   y_vect = np.cross(up,x_vect) # (x,y,z)
    #   z_vect = np.cross(x_vect,y_vect) # (x,y,z)

    #   z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)
    #   # z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)+x_vect*np.dot(x_vect,z_vect)*(1-m.cos(roll))

    #   y_rot = np.cross(z_rot, x_vect)


    # elif frameList[storedFrameId] == "NED":
    #   pass
    #   ##### perform axis computations #####################
    #   down=np.array([0,0,1]) # (x,y,z)
    #   x_vect=np.array([m.cos(-yaw)*m.cos(-pitch), m.sin(-yaw)*m.cos(-pitch), -1.00*m.sin(-pitch)]) # (x,y,z)
    #   y_vect = np.cross(down,x_vect) # (x,y,z)
    #   z_vect = np.cross(x_vect,y_vect) # (x,y,z)

    #   z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)
    #   # z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)+x_vect*np.dot(x_vect,z_vect)*(1-m.cos(roll))

    #   y_rot = np.cross(z_rot, x_vect)


    ##### perform axis computations #####################
    up=np.array([0,0,1]) # (x,y,z)
    x_vect=np.array([m.cos(yaw)*m.cos(pitch), m.sin(yaw)*m.cos(pitch), -1.00*m.sin(pitch)]) # (x,y,z)
    y_vect = np.cross(up,x_vect) # (x,y,z)
    z_vect = np.cross(x_vect,y_vect) # (x,y,z)

    z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)
    # z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)+x_vect*np.dot(x_vect,z_vect)*(1-m.cos(roll))

    y_rot = np.cross(z_rot, x_vect)

    ######### draw axis in vpyton ########################
    xArrow.axis = vector(x_vect[1], x_vect[2], x_vect[0])# (y,z,x)
    xArrow.length = 3

    yArrow.axis = vector(y_rot[1], y_rot[2], y_rot[0])# (y,z,x)
    yArrow.length = 2

    zArrow.axis = vector(z_rot[1], z_rot[2], z_rot[0])# (y,z,x)
    zArrow.length = 1.5

    myObj.axis = vector(x_vect[1], x_vect[2], x_vect[0]) # (y,z,x)
    myObj.up = vector(z_rot[1], z_rot[2], z_rot[0]) # (y,z,x)

  ##----------------------------------------------------------------##



if __name__ == "__main__":
  main()