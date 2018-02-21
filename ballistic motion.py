import math as ma
import numpy as np

grav = -9.81
vel = int(input("Enter the initial velocity in m/s: "))
ang = int(input("Enter the initial angle in degrees: "))
y = int(input("Enter the initial height in meters: "))
theta = ang*(ma.pi/180)

def y_position(y, vel, theta, grav, time):
    ypos = y + vel*ma.sin(theta)*time + (g*time**2)/2
    return ypos

def x_position(vel, theta, time):
    xpos = vel*ma.cos(theta)*time
    return xpos

time = np.linspace(0,10,100)
list_xpos = []
list_ypos = []

for a in time:
    list_xpos.append(x_position(vel, theta, time))
    list_ypos.append(y_position(y, vel, theta, grav, time))

print (list_xpos)
print (list_ypos)
