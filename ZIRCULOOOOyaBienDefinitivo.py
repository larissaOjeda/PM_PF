#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def orientate (xgoal, ygoal,i):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = -(math.pi/2)-.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = 0.0
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', i, 'y=', y)

        if (dtheta < 0.01):
            break

def go_to_goal (xgoal, ygoal,i):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 0.5				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = -(math.pi/2)-.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', i, 'y=', y)

        if (distance < 0.01):
            break

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)     
	radio=4.5
	xoriginal=x
	yoriginal=y
	rotacion=0
	global i
	
	inicio=0
	final=361
	salto=10

	if(rotacion==1):
		for i in range(0,361,10):
			if((abs(i)>=0 and abs(i)<90)):
					
				xn = xoriginal+radio*math.cos((i*math.pi)/180)
				yn = yoriginal+radio*math.sin((i*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>90 and abs(i)<=180):
				xn = xoriginal-radio*math.sin(((i-90)*math.pi)/180)
				yn = yoriginal+radio*math.cos(((i-90)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>=180 and abs(i)<=270):
				xn = xoriginal-radio*math.cos(((i-180)*math.pi)/180)
				yn = yoriginal-radio*math.sin(((i-180)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>=270 and abs(i)<361):
				xn = xoriginal+radio*math.sin(((i-270)*math.pi)/180)
				yn = yoriginal-radio*math.cos(((i-270)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)



	
	if(rotacion==0):
		for i in range(0,361,10):
			if((abs(i)>=0 and abs(i)<90)):
					
				xn = xoriginal+radio*math.cos(((-i)*math.pi)/180)
				yn = yoriginal+radio*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>=90 and abs(i)<180):
					
				
				xn = xoriginal+radio*math.cos(((i)*math.pi)/180)
				yn = yoriginal-radio*math.sin(((i)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>=180 and abs(i)<270):
				xn = xoriginal+radio*math.cos(((-i)*math.pi)/180)
				yn = yoriginal+radio*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)
			if(abs(i)>=270 and abs(i)<361):
				xn = xoriginal+radio*math.cos(((-i)*math.pi)/180)
				yn = yoriginal+radio*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn,i)
				go_to_goal(xn,yn,i)

		

				

    except rospy.ROSInterruptException:        
	pass
