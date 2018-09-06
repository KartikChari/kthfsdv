#!/usr/bin/env python
# Written by: Kartik Chari
# Date: 02 Sept 2018
# This is a publisher node A that publishes k>0 every 0.05 Hz and in every iteration, the value of k increases by n=4

# Imorting dependencies and required message types
import rospy
from std_msgs.msg import Float32
k = Float32()

# Function Definition
def start():
	# node initialization
	rospy.init_node("Broadcast")
	# creating a publisher object
	k_pub = rospy.Publisher("Chari",Float32,queue_size=1)
	# setting the broadcasting frequency to 0.05 Hz
	r = rospy.Rate(0.05)
	# variable initialization and assignment
	k = -3.0
	n = 4.0
	# Condition for the loop
	while not rospy.is_shutdown():
		k = k + n
		k_pub.publish(k)
		r.sleep()

# Function call
start()
